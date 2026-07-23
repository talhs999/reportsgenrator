"""
German Vehicle History Report PDF Generator.
Generates comprehensive German language reports (Fahrzeug-Historienbericht) using Playwright.
"""
import os
import base64
import logging
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
from starlette.concurrency import run_in_threadpool

from config import TEMPLATE_DIR, UPLOAD_DIR, STATIC_DIR
from api.germany_scraper import scrape_germany_vehicle_data

def _file_to_data_uri(file_path: str) -> str:
    """Convert a local file to a base64 Data URI."""
    if not file_path or not os.path.exists(file_path):
        return ""
    ext = os.path.splitext(file_path)[1].lower().replace('.', '')
    mime_types = {
        'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg',
        'svg': 'image/svg+xml', 'webp': 'image/webp'
    }
    mime = mime_types.get(ext, 'image/png')
    with open(file_path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

def _html_to_pdf_sync(html_content: str) -> bytes:
    """Convert HTML string to PDF synchronously using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )
        page = browser.new_page()
        page.set_content(html_content, wait_until="networkidle")

        pdf_bytes = page.pdf(
            format="A4",
            print_background=True,
            margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"},
            display_header_footer=False,
        )

        browser.close()
        return pdf_bytes

from api.germany_templated import (
    get_stolen_finance_writeoff_de,
    get_service_history_simulation_de,
    get_detailed_prepurchase_de,
    get_component_assessment_de,
    get_running_costs_de,
    get_glossary_de
)

def _build_toc_de(p: dict) -> list:
    """Build table of contents for Germany report."""
    toc = []
    def add_sec(title, key):
        if p.get(key) is not None:
            if isinstance(p[key], list) and len(p[key]) > 0:
                toc.append({"title": title, "page": p[key][0]})
            elif isinstance(p[key], int):
                toc.append({"title": title, "page": p[key]})
    
    add_sec("1. Fahrzeugidentität & KBA-Daten", "identity")
    add_sec("2. Diebstahl- & Finanzierungscheck", "stolen_finance")
    add_sec("3. Laufende Kosten & Wertverlust", "running_costs")
    add_sec("4. Wartungshistorie (Simuliert)", "service_history")
    add_sec("5. Mechanische Zustandsprüfung", "component_assessment")
    add_sec("6. 100-Punkte Gebrauchtwagen-Check", "prepurchase")
    add_sec("7. Automobil-Glossar", "glossary")
    add_sec("8. Haftungsausschluss", "disclaimer")
    
    return sorted(toc, key=lambda x: x["page"])

def _calculate_pages_de(package: str) -> dict:
    """Calculate pages to hit exactly 15, 20, or 25+ based on package."""
    p = {}
    current = 1
    
    p['cover'] = current
    current += 1
    p['toc'] = current
    current += 1
    
    # Always included (Basic)
    p['identity'] = current
    current += 1
    p['stolen_finance'] = current
    current += 1
    
    # Standard & Premium additions
    if package in ['standard', 'premium']:
        p['running_costs'] = current
        current += 1
        p['component_assessment'] = current
        current += 1
    else:
        p['running_costs'] = None
        p['component_assessment'] = None
        
    # Premium additions
    if package == 'premium':
        # Service history spans multiple pages
        p['service_history'] = [current, current+1]
        current += 2
        # Pre-purchase spans multiple pages
        p['prepurchase'] = [current, current+1, current+2]
        current += 3
        # Glossary
        p['glossary'] = current
        current += 1
    else:
        p['service_history'] = None
        p['prepurchase'] = None
        p['glossary'] = None
        
    # Disclaimer always last
    p['disclaimer'] = current
    
    # Pad to reach exactly 15, 20, or 25 if necessary using CSS in template
    # Basic = ~15, Standard = ~20, Premium = ~25
    return p

async def generate_germany_report(
    vin: str,
    package: str = "standard",
    primary_color: str = "#1a3a5c",
    accent_color: str = "#c8a45a",
    cover_logo_filename: str = None,
    header_logo_filename: str = None,
    company_name: str = "Deutscher Fahrzeugdienst",
    website_url: str = "",
    insurance_status: str = "not_checked",
) -> bytes:
    """
    Generate a German Vehicle History Report PDF.
    """
    # 1. Fetch Vehicle Data via German Scraper
    vehicle_data = await scrape_germany_vehicle_data(vin)
    if not vehicle_data.get("success"):
        raise ValueError(vehicle_data.get("error", "Fahrzeugdaten konnten nicht abgerufen werden."))

    # 2. Prepare Logos & Assets
    cover_logo_uri = _file_to_data_uri(os.path.join(UPLOAD_DIR, cover_logo_filename)) if cover_logo_filename else None
    header_logo_uri = _file_to_data_uri(os.path.join(UPLOAD_DIR, header_logo_filename)) if header_logo_filename else None
    
    bg_path = os.path.join(STATIC_DIR, 'images', 'cover_background.png')
    cover_bg_uri = _file_to_data_uri(bg_path)

    report_date = datetime.now().strftime("%d.%m.%Y")
    
    # Generate maximum synthetic data
    simulated_mileage = 120000 # default
    stolen_finance = get_stolen_finance_writeoff_de(vin)
    service_history = get_service_history_simulation_de(simulated_mileage) if package == 'premium' else None
    prepurchase = get_detailed_prepurchase_de() if package == 'premium' else None
    component_assessment = get_component_assessment_de() if package in ['standard', 'premium'] else None
    running_costs = get_running_costs_de() if package in ['standard', 'premium'] else None
    glossary = get_glossary_de() if package == 'premium' else None
    
    pages = _calculate_pages_de(package)
    toc = _build_toc_de(pages)

    # 3. Context Preparation
    context = {
        "registration": vin.upper(),
        "package": package,
        "report_date": report_date,
        "report_id": f"FIN-DE-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "primary_color": primary_color,
        "accent_color": accent_color,
        "cover_logo_uri": cover_logo_uri,
        "header_logo_uri": header_logo_uri,
        "cover_bg_uri": cover_bg_uri,
        "company_name": company_name,
        "vehicle": vehicle_data,
        "website_url": website_url,
        "pages": pages,
        "toc": toc,
        "stolen_finance": stolen_finance,
        "service_history": service_history,
        "prepurchase": prepurchase,
        "component_assessment": component_assessment,
        "running_costs": running_costs,
        "glossary": glossary
    }

    # 4. Render HTML Template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report_de.html")
    html_content = template.render(**context)

    # 5. Render PDF with Playwright synchronously in a threadpool
    pdf_bytes = await run_in_threadpool(_html_to_pdf_sync, html_content)
    
    return pdf_bytes
