"""
Configuration for the UK Vehicle History Report System.
All API keys and settings are managed here.
"""
import os

# ─── DVLA VES API ───────────────────────────────────────────────
# Register at: https://developer-portal.driver-vehicle-licensing.api.gov.uk/
# Get your API key from the portal after registration (free).

# ─── DVSA MOT History API ──────────────────────────────────────
# Register at: https://dvsa.github.io/mot-history-api-documentation/
# Get your API key + Client ID from the MOT History API portal (free).
# We are using web scraping now, so API keys are no longer strictly required.
# They have been removed to enforce the scraper engine.

# Branding & Theme defaults
DEFAULT_PRIMARY_COLOR = os.getenv("PRIMARY_COLOR", "#1e3a8a")
DEFAULT_ACCENT_COLOR = os.getenv("ACCENT_COLOR", "#3b82f6")
DEFAULT_COMPANY_NAME = os.getenv("COMPANY_NAME", "UK Vehicle Data Services")
REPORT_VERSION = "1.0"

# ─── Paths ──────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
TEMPLATE_DIR = os.path.join(BASE_DIR, "report", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
FRONTEND_TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)
