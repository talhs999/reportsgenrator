"""
UK Vehicle History Report System — Main FastAPI Application.

This is the main entry point. It serves:
1. The frontend web app (HTML form)
2. The PDF report generation API endpoint
3. Static files (CSS, JS, uploads)

Run with: uvicorn main:app --reload --port 8000
"""
import os
import uuid
from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import io

from config import UPLOAD_DIR, FRONTEND_TEMPLATE_DIR, STATIC_DIR
from report.generator import generate_report

from fastapi import Request
from fastapi.responses import JSONResponse
import traceback

# ── Create App ──────────────────────────────────────────────────
app = FastAPI(
    title="UK Vehicle History Report Generator",
    description="Generate comprehensive vehicle history reports from DVLA & DVSA data.",
    version="1.0.0",
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    err_msg = traceback.format_exc()
    print("Global Exception:", err_msg)
    return JSONResponse(
        status_code=500,
        content={"error": f"Global Server Error: {str(exc)}", "traceback": err_msg}
    )


# ── Static Files ───────────────────────────────────────────────
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(os.path.join(STATIC_DIR, "css"), exist_ok=True)
os.makedirs(os.path.join(STATIC_DIR, "js"), exist_ok=True)
os.makedirs(FRONTEND_TEMPLATE_DIR, exist_ok=True)

DOWNLOADS_DIR = os.path.join(STATIC_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ── Routes ──────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the frontend web app as a static HTML file."""
    index_path = os.path.join(FRONTEND_TEMPLATE_DIR, "index.html")
    return FileResponse(index_path, media_type="text/html")


@app.post("/api/generate-report")
async def api_generate_report(
    registration: str = Form(...),
    package: str = Form("standard"),
    primary_color: str = Form("#1a3a5c"),
    accent_color: str = Form("#c8a45a"),
    company_name: str = Form("Vehicle History Reports"),
    website_url: str = Form(""),
    insurance_status: str = Form("not_checked"),
    cover_logo: UploadFile = File(None),
    header_logo: UploadFile = File(None),
):
    """
    Generate a vehicle history report PDF.
    
    Accepts form data with:
    - registration: UK vehicle registration number
    - package: 'standard' or 'premium'
    - primary_color: Hex color for theme
    - accent_color: Hex color for accents
    - company_name: Company name to display
    - cover_logo: Optional logo for the front cover
    - header_logo: Optional logo for inner pages
    """
    try:
        # Handle logo uploads
        cover_logo_filename = None
        if cover_logo and cover_logo.filename:
            ext = os.path.splitext(cover_logo.filename)[1].lower()
            if ext in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'):
                cover_logo_filename = f"cover_{uuid.uuid4().hex}{ext}"
                logo_path = os.path.join(UPLOAD_DIR, cover_logo_filename)
                content = await cover_logo.read()
                with open(logo_path, "wb") as f:
                    f.write(content)

        header_logo_filename = None
        if header_logo and header_logo.filename:
            ext = os.path.splitext(header_logo.filename)[1].lower()
            if ext in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'):
                header_logo_filename = f"header_{uuid.uuid4().hex}{ext}"
                logo_path = os.path.join(UPLOAD_DIR, header_logo_filename)
                content = await header_logo.read()
                with open(logo_path, "wb") as f:
                    f.write(content)

        # Generate PDF
        pdf_bytes = await generate_report(
            registration=registration,
            package=package,
            primary_color=primary_color,
            accent_color=accent_color,
            cover_logo_filename=cover_logo_filename,
            header_logo_filename=header_logo_filename,
            company_name=company_name,
            website_url=website_url,
            insurance_status=insurance_status,
        )

        # Return JSON with download URL
        reg_clean = registration.upper().replace(" ", "")
        filename = f"Vehicle_Report_{reg_clean}.pdf"
        download_id = uuid.uuid4().hex
        pdf_path = os.path.join(DOWNLOADS_DIR, f"{download_id}.pdf")
        
        with open(pdf_path, "wb") as f:
            f.write(pdf_bytes)
            
        return JSONResponse(content={
            "success": True,
            "download_url": f"/api/download/{download_id}?filename={filename}"
        })

    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": f"Report generation failed: {str(e)}"})


@app.get("/api/download/{download_id}")
async def download_report(download_id: str, filename: str = "Vehicle_Report.pdf"):
    """Download a generated report by ID."""
    pdf_path = os.path.join(DOWNLOADS_DIR, f"{download_id}.pdf")
    if not os.path.exists(pdf_path):
        return JSONResponse(status_code=404, content={"error": "Download link expired or invalid."})
    return FileResponse(pdf_path, media_type="application/pdf", filename=filename)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok", "service": "Vehicle History Report Generator"}
