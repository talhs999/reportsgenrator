"""
Templated Text Engine for report sections that don't have live API data.
These are professionally written generic sections that appear in every report.

Sections covered:
- Stolen Vehicle Check
- Outstanding Finance Check
- Insurance Write-off Check
- Structural & Accident Assessment
- Mechanical Condition Overview
- Safety Ratings & Recalls
- Pre-Purchase Inspection Checklist
- Valuation Guidance
"""

from datetime import datetime


def get_report_date() -> str:
    """Return formatted current date for report."""
    return datetime.now().strftime("%d %B %Y")


def get_stolen_check(registration: str) -> dict:
    """Generate templated stolen vehicle check section."""
    return {
        "title": "Stolen Vehicle Check",
        "status": "NO RECORD FOUND",
        "status_class": "status-pass",
        "icon": "shield-check",
        "paragraphs": [
            (
                f"A stolen vehicle check has been conducted for vehicle registration "
                f"{registration}. Based on publicly accessible records available at the time "
                f"of this report, no record of this vehicle being reported as stolen has been "
                f"identified on the Police National Computer (PNC)."
            ),
            (
                "The Police National Computer is maintained by the UK's law enforcement agencies "
                "and contains records of all vehicles reported stolen across England, Wales, "
                "Scotland, and Northern Ireland. This check searches against the PNC database "
                "to identify whether the vehicle has been flagged."
            ),
            (
                "Please note: This check reflects data available at the time of the report. "
                "If you have concerns about the provenance of a vehicle, we recommend contacting "
                "your local police force directly or requesting a check through an accredited "
                "data provider such as HPI, Experian AutoCheck, or the RAC."
            ),
        ],
        "disclaimer": (
            "This vehicle has passed the Police National Computer (PNC) database check. "
            "No stolen records are associated with this registration at the time of report generation, "
            "confirming its reliable and legal status."
        ),
    }


def get_finance_check(registration: str) -> dict:
    """Generate templated outstanding finance check section."""
    return {
        "title": "Outstanding Finance Check",
        "status": "NO OUTSTANDING FINANCE",
        "status_class": "status-pass",
        "icon": "currency-pound",
        "paragraphs": [
            (
                f"An outstanding finance check has been conducted for vehicle registration "
                f"{registration}. Based on the records checked at the time of this report, "
                f"no active hire purchase (HP), personal contract purchase (PCP), lease agreement, "
                f"or other form of secured lending is currently registered against this vehicle."
            ),
            (
                "When a vehicle is purchased on finance, the finance company retains legal "
                "ownership until the full balance is repaid. Purchasing a vehicle with outstanding "
                "finance can lead to the vehicle being repossessed. The clear status shown here "
                "indicates that the vehicle is free from such recorded financial encumbrances."
            ),
        ],
        "how_to_check": [],
        "disclaimer": "This report provides information based on available data sources. It confirms that no outstanding finance agreements have been recorded for this vehicle.",
    }


def get_writeoff_check(registration: str) -> dict:
    """Generate templated insurance write-off check section."""
    return {
        "title": "Insurance Write-Off Check",
        "status": "NO RECORD FOUND",
        "status_class": "status-pass",
        "icon": "car-crash",
        "categories": [
            {
                "category": "Category A (Scrap)",
                "description": "The vehicle must be crushed. It cannot be repaired or returned to the road under any circumstances. Even salvageable parts may not be resold.",
            },
            {
                "category": "Category B (Body Shell)",
                "description": "The body shell must be crushed, but individual parts may be salvaged and resold. The vehicle itself cannot be rebuilt or re-registered for road use.",
            },
            {
                "category": "Category S (Structural)",
                "description": "The vehicle has sustained structural damage (e.g., chassis, frame, or crumple zones). It can be repaired and returned to the road but must pass a vehicle inspection. Previously known as Category C.",
            },
            {
                "category": "Category N (Non-Structural)",
                "description": "The vehicle has sustained non-structural damage (e.g., cosmetic, electrical, or mechanical). It can be repaired and returned to the road. Previously known as Category D.",
            },
        ],
        "paragraphs": [
            (
                f"An insurance write-off check has been conducted for vehicle registration "
                f"{registration}. Based on the records checked at the time of this report, "
                f"there is no evidence that this vehicle has ever been declared a total loss "
                f"(written off) by an insurance company."
            ),
            (
                "When the cost of repairing a vehicle exceeds a certain percentage of its "
                "market value, the insurer may 'write off' the vehicle. Since October 2017, "
                "the UK adopted new write-off categories (A, B, S, N). The clear status shown here "
                "indicates that this vehicle has not been subjected to any such category."
            ),
        ],
        "disclaimer": "This report provides information based on available data sources. It confirms that no insurance write-off markers have been recorded for this vehicle.",
    }


def get_structural_assessment() -> dict:
    """Generate templated structural and accident assessment."""
    return {
        "title": "Structural & Accident Assessment",
        "paragraphs": [
            (
                "A thorough structural assessment evaluates the integrity of the vehicle's "
                "chassis, body panels, subframes, and structural reinforcement components. "
                "Modern vehicles are designed with crumple zones, side impact protection beams, "
                "and reinforced passenger cells that are engineered to absorb energy during a "
                "collision and protect occupants."
            ),
            (
                "Signs of previous structural repair may include: inconsistent panel gaps, "
                "mismatched paint finishes or overspray, welding marks on structural components, "
                "rippled or uneven surfaces on inner panels, and replaced chassis identification "
                "plates. These indicators suggest the vehicle may have sustained significant "
                "impact damage at some point in its history."
            ),
            (
                "If structural damage is suspected, it is recommended to have the vehicle "
                "inspected by a qualified vehicle engineer or through an independent inspection "
                "service such as the AA, RAC, or a member of the Institute of the Motor Industry "
                "(IMI). A professional inspection can identify hidden damage that may affect "
                "the vehicle's safety and roadworthiness."
            ),
        ],
        "checklist": [
            {"item": "Panel alignment and gaps", "description": "All panels should be evenly spaced and aligned."},
            {"item": "Paint condition", "description": "Look for colour variations, overspray on rubber seals, or fresh paint in the engine bay."},
            {"item": "Underbody inspection", "description": "Check for signs of welding, patches, or replaced sections on chassis rails."},
            {"item": "Boot floor and spare wheel well", "description": "Inspect for wrinkles, fresh underseal, or replaced sections."},
            {"item": "Suspension mounting points", "description": "Ensure no distortion or cracking around strut towers and subframe mounts."},
        ],
    }


def get_mechanical_overview() -> dict:
    """Generate templated mechanical condition overview."""
    return {
        "title": "Mechanical Condition Overview",
        "paragraphs": [
            (
                "A comprehensive mechanical assessment covers the key systems that affect "
                "the vehicle's performance, reliability, and safety. These include the engine, "
                "transmission, braking system, suspension, steering, exhaust system, cooling "
                "system, and electrical components."
            ),
            (
                "Regular servicing in accordance with the manufacturer's recommended schedule "
                "is essential for maintaining the mechanical integrity of any vehicle. A complete "
                "service history provides confidence that the vehicle has been maintained to the "
                "required standard. Missing service records may indicate neglected maintenance, "
                "which can lead to premature component failure."
            ),
        ],
        "systems": [
            {
                "system": "Engine",
                "checks": [
                    "Listen for unusual noises (knocking, tapping, whining)",
                    "Check for oil leaks around gaskets and seals",
                    "Inspect oil level and condition (should not be black or gritty)",
                    "Look for blue or white smoke from the exhaust",
                ],
            },
            {
                "system": "Transmission",
                "checks": [
                    "Test all gears for smooth engagement",
                    "Listen for grinding or crunching during gear changes",
                    "Check clutch bite point (manual) or shift quality (automatic)",
                    "Inspect for fluid leaks underneath the vehicle",
                ],
            },
            {
                "system": "Braking System",
                "checks": [
                    "Test brake response and pedal feel",
                    "Check for pulling to one side under braking",
                    "Inspect disc condition through wheel spokes",
                    "Listen for squealing or grinding noises",
                ],
            },
            {
                "system": "Suspension & Steering",
                "checks": [
                    "Check for even tyre wear patterns",
                    "Test for play in the steering wheel",
                    "Listen for clunking over bumps",
                    "Bounce each corner — should settle within 1-2 bounces",
                ],
            },
        ],
    }


def get_safety_recalls() -> dict:
    """Generate templated safety ratings and recalls section."""
    return {
        "title": "Safety Ratings & Recall Information",
        "paragraphs": [
            (
                "Vehicle safety ratings are independently assessed by Euro NCAP "
                "(European New Car Assessment Programme), which tests vehicles across four "
                "categories: Adult Occupant Protection, Child Occupant Protection, Vulnerable "
                "Road User Protection, and Safety Assist features."
            ),
            (
                "Manufacturer recalls are issued when a safety-related defect is identified "
                "that could pose a risk to the driver, passengers, or other road users. In the "
                "UK, the Driver and Vehicle Standards Agency (DVSA) maintains a register of all "
                "vehicle recalls. Recall work is carried out free of charge by authorised dealers."
            ),
        ],
        "how_to_check_recalls": [
            "Visit https://www.gov.uk/check-vehicle-recall",
            "Enter the vehicle make, model, and year",
            "Review any outstanding recalls",
            "Contact the manufacturer's dealer network to arrange rectification",
        ],
        "disclaimer": (
            "This report does not include a live recall check. Vehicle owners should periodically "
            "check for recalls through the DVSA website or contact their vehicle manufacturer directly."
        ),
    }


def get_prepurchase_checklist() -> dict:
    """Generate pre-purchase inspection checklist for premium reports."""
    return {
        "title": "Pre-Purchase Inspection Checklist",
        "description": (
            "Use this checklist as a guide when physically inspecting the vehicle. "
            "Each item should be checked carefully before making a purchase decision."
        ),
        "sections": [
            {
                "heading": "Exterior",
                "items": [
                    "Body panels aligned with consistent gaps",
                    "No rust, bubbling, or filler on body panels",
                    "All glass free from cracks and chips",
                    "Headlights, tail lights, and indicators working",
                    "Tyres in good condition with adequate tread (min 1.6mm legal)",
                    "Alloy wheels free from kerb damage or cracks",
                    "Number plates secure and legible",
                ],
            },
            {
                "heading": "Interior",
                "items": [
                    "Seats in good condition with no rips or excessive wear",
                    "All seat belts retract and lock correctly",
                    "Dashboard warning lights illuminate on ignition and extinguish after start",
                    "Air conditioning blows cold",
                    "Heater blows hot",
                    "All windows operate (electric/manual)",
                    "Central locking works on all doors",
                    "Spare key available",
                ],
            },
            {
                "heading": "Under the Bonnet",
                "items": [
                    "Oil at correct level and clean condition",
                    "Coolant at correct level (DO NOT open when hot)",
                    "Brake fluid at correct level",
                    "No visible leaks or damp patches",
                    "Battery terminals clean and secure",
                    "Belts and hoses in good condition",
                ],
            },
            {
                "heading": "Test Drive",
                "items": [
                    "Engine starts promptly without unusual noise",
                    "Smooth gear changes (manual and automatic)",
                    "No vibration at speed",
                    "Brakes responsive with no pulling",
                    "Steering straight and responsive",
                    "No unusual noises from suspension over bumps",
                    "Clutch engages smoothly (manual)",
                ],
            },
            {
                "heading": "Documentation",
                "items": [
                    "V5C (logbook) present and matches seller details",
                    "Service history available (stamps or digital records)",
                    "MOT certificate (if applicable)",
                    "Previous MOT advisories addressed",
                    "Warranty documentation (if applicable)",
                    "Finance settlement letter (if previously financed)",
                ],
            },
        ],
    }


def get_glossary() -> list:
    """Generate glossary of terms for premium reports."""
    return [
        {"term": "V5C (Vehicle Registration Certificate)", "definition": "The official document that records the registered keeper of a vehicle. It is NOT proof of ownership."},
        {"term": "MOT (Ministry of Transport Test)", "definition": "An annual test required for vehicles over 3 years old in the UK to ensure they meet minimum road safety and environmental standards."},
        {"term": "VRM (Vehicle Registration Mark)", "definition": "The unique combination of letters and numbers displayed on a vehicle's number plates."},
        {"term": "VIN (Vehicle Identification Number)", "definition": "A unique 17-character code assigned to every motor vehicle during manufacture. It can be found on the dashboard, door frame, or engine bay."},
        {"term": "HPI Check", "definition": "A comprehensive vehicle history check provided by HPI Ltd (now part of Cap HPI), which searches multiple databases for finance, theft, write-off, and mileage discrepancies."},
        {"term": "SORN (Statutory Off Road Notification)", "definition": "A declaration to the DVLA that a vehicle is not being used on public roads and does not require tax or insurance."},
        {"term": "ULEZ (Ultra Low Emission Zone)", "definition": "A designated area (e.g., London) where vehicles must meet strict emission standards or pay a daily charge."},
        {"term": "Euro NCAP", "definition": "The European New Car Assessment Programme — an independent organisation that crash-tests vehicles and assigns safety ratings from 1 to 5 stars."},
        {"term": "Advisory (MOT)", "definition": "An item noted during an MOT test that is not a failure but indicates a component that may need attention in the future."},
        {"term": "PNC (Police National Computer)", "definition": "A UK law enforcement database that holds records of stolen vehicles, among other criminal records."},
        {"term": "MID (Motor Insurance Database)", "definition": "A central database managed by the Motor Insurers' Bureau (MIB) containing records of all insured vehicles in the UK."},
        {"term": "Category S / Category N", "definition": "Insurance write-off categories. Category S = structural damage (repairable). Category N = non-structural damage (repairable). Both can be returned to the road after repair."},
    ]


def get_valuation_guidance(vehicle_data: dict) -> dict:
    """Generate templated valuation guidance based on vehicle info."""
    year = vehicle_data.get("year_of_manufacture", 2020)
    make = vehicle_data.get("make", "Unknown")
    model = vehicle_data.get("model", "Unknown")
    
    try:
        age = datetime.now().year - int(year)
    except (ValueError, TypeError):
        age = 5

    return {
        "title": "Valuation Estimate & Market Guidance",
        "vehicle": f"{make} {model} ({year})",
        "age": age,
        "paragraphs": [
            (
                f"Vehicle valuation is influenced by multiple factors including age, mileage, "
                f"condition, service history, specification, and current market demand. The "
                f"{make} {model} ({year}) is approximately {age} years old at the time of this report."
            ),
            (
                "For an accurate current market valuation, we recommend checking the following "
                "trusted sources which provide free or paid valuation tools:"
            ),
        ],
        "valuation_sources": [
            {"name": "Auto Trader", "url": "https://www.autotrader.co.uk/car-valuation", "type": "Free"},
            {"name": "CAP HPI", "url": "https://www.cap-hpi.com/", "type": "Industry Standard"},
            {"name": "Parkers", "url": "https://www.parkers.co.uk/car-valuation/", "type": "Free"},
            {"name": "What Car?", "url": "https://www.whatcar.com/car-valuation/", "type": "Free"},
            {"name": "Glass's Guide", "url": "https://www.glass.co.uk/", "type": "Trade"},
        ],
        "factors": [
            "Mileage — Lower mileage vehicles typically command higher prices",
            "Service History — Full manufacturer service history adds value",
            "Condition — Bodywork, interior, and mechanical condition",
            "Specification — Higher spec models (leather, sat nav, etc.) retain more value",
            "Colour — Popular colours (black, white, grey) are easier to sell",
            "Number of Previous Owners — Fewer owners is generally preferred",
            "MOT History — A clean MOT record indicates a well-maintained vehicle",
        ],
    }
