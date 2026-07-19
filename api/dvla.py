"""
DVLA Vehicle Enquiry Service (VES) API Client.
Official UK Government API - FREE to use.

Register at: https://developer-portal.driver-vehicle-licensing.api.gov.uk/
This API provides: Make, Model, Colour, Year, Engine Size, Fuel Type,
Tax Status, Tax Due Date, MOT Status, MOT Expiry, CO2 Emissions, etc.
"""
import logging

logger = logging.getLogger(__name__)


async def fetch_vehicle_data(registration: str) -> dict:
    """
    Fetch basic vehicle data using the scraper engine.
    """
    from api.scraper_engine import scrape_vehicle_data
    
    # Use the scraper to get all data
    return await scrape_vehicle_data(registration)


def _determine_vehicle_type(data: dict) -> str:
    """Determine if vehicle is car, motorcycle, van, etc."""
    wheelplan = data.get("wheelplan", "").upper()
    body_type = data.get("typeApproval", "").upper()
    
    if body_type in ("L1", "L2", "L3", "L4", "L5"):
        return "Motorcycle"
    elif body_type in ("N1", "N2", "N3"):
        return "Van / Commercial"
    elif wheelplan and "2 AXLE" in wheelplan:
        return "Car"
    else:
        return "Car"


def get_demo_data(registration: str) -> dict:
    """
    Return demo/sample data for testing when API key is not set.
    This allows the system to work without a real API key.
    """
    reg = registration.upper().replace(" ", "")
    import re
    if not re.match(r"^[A-Z0-9]{2,7}$", reg) or reg in ("INVALID", "NOTFOUND", "TEST"):
        return {"success": False, "error": "Vehicle not found or invalid registration."}

    return {
        "success": True,
        "registration": reg,
        "make": "BMW",
        "model": "320D",
        "colour": "BLACK",
        "year_of_manufacture": 2019,
        "month_of_first_registration": "2019-03",
        "date_of_first_registration": "2019-03",
        "engine_capacity": 1995,
        "fuel_type": "DIESEL",
        "co2_emissions": 117,
        "euro_status": "EURO 6",
        "tax_status": "Taxed",
        "tax_due_date": "2025-03-01",
        "mot_status": "Valid",
        "mot_expiry_date": "2025-09-15",
        "type_approval": "M1",
        "wheelplan": "2 AXLE RIGID BODY",
        "revenue_weight": 0,
        "real_driving_emissions": "RDE2",
        "date_of_last_v5c_issued": "2023-06-12",
        "marked_for_export": False,
        "vehicle_type": "Car",
    }
