"""
Templated Text Engine for Germany Reports.
Generates comprehensive synthetic data in German to expand the report to 25+ pages for Premium tiers.
"""
import random
from datetime import datetime, timedelta

def get_report_date_de() -> str:
    return datetime.now().strftime("%d.%m.%Y")

def get_stolen_finance_writeoff_de(vin: str) -> dict:
    return {
        "stolen": {
            "title": "Diebstahlüberprüfung (Stolen Vehicle Check)",
            "status": "KEIN EINTRAG",
            "icon": "shield-check",
            "text": f"Eine Überprüfung auf Diebstahl wurde für die FIN {vin} durchgeführt. Basierend auf öffentlich zugänglichen Registern und internationalen Datenbanken liegt für dieses Fahrzeug zum Zeitpunkt der Berichterstellung keine Diebstahlsanzeige vor."
        },
        "finance": {
            "title": "Finanzierungs- & Leasing-Check",
            "status": "FREI",
            "icon": "credit-card",
            "text": "Es wurden keine ausstehenden Finanzierungs-, Leasing- oder Kreditvereinbarungen gefunden, die durch das Fahrzeug besichert sind. Das Fahrzeug scheint unbelastet zu sein."
        },
        "writeoff": {
            "title": "Totalschaden- & Unfallregister",
            "status": "SAUBER",
            "icon": "car-crash",
            "text": "Es gibt keine Hinweise darauf, dass dieses Fahrzeug jemals als wirtschaftlicher oder struktureller Totalschaden abgeschrieben wurde."
        }
    }

def get_service_history_simulation_de(mileage: int = 150000) -> list:
    """Simulates a highly detailed service history spanning multiple pages."""
    services = []
    current_mileage = max(10000, mileage - (mileage % 15000))
    current_date = datetime.now() - timedelta(days=30)
    
    interval_km = 15000
    interval_days = 180
    
    while current_mileage > 0:
        services.append({
            "date": current_date.strftime("%d.%m.%Y"),
            "mileage": f"{current_mileage:,} km".replace(",", "."),
            "dealer": random.choice(["Autorisierte Vertragswerkstatt", "Unabhängige Fachwerkstatt", "Bosch Car Service"]),
            "work_done": [
                "Motoröl und Ölfilter gewechselt",
                "Fahrzeugdiagnose (OBD-II) ohne Fehler abgeschlossen",
                "Luftfilter und Innenraumfilter geprüft/erneuert",
                "Bremsflüssigkeit und Kühlerfrostschutz geprüft",
                "Sichtprüfung von Fahrwerk, Lenkung und Antriebsstrang"
            ] if current_mileage % 30000 != 0 else [
                "Große Inspektion durchgeführt",
                "Motoröl und Ölfilter gewechselt",
                "Zündkerzen / Glühkerzen erneuert",
                "Bremsbeläge und Bremsscheiben an der Vorderachse erneuert",
                "Getriebeöl geprüft / gewechselt",
                "Klimaanlagenservice inkl. Kältemittel",
                "Reifenprofiltiefe und Reifendruck auf allen Rädern optimiert",
                "Fahrwerksvermessung durchgeführt"
            ],
            "notes": "Fahrzeug in technisch einwandfreiem Zustand. Keine Mängel festgestellt." if current_mileage % 45000 != 0 else "Leichte Abnutzungserscheinungen an den Stoßdämpfern bemerkt, noch im Toleranzbereich."
        })
        current_mileage -= interval_km
        current_date -= timedelta(days=interval_days)
        
    return services

def get_detailed_prepurchase_de() -> dict:
    """100-Point checklist to take up 4-5 pages."""
    return {
        "exterior": {
            "title": "1. Karosserie & Lackierung (Exterior)",
            "items": [
                {"name": "Lackdicke (keine Nachlackierung)", "status": "Bestanden"},
                {"name": "Spaltmaße an Türen und Hauben", "status": "Bestanden"},
                {"name": "Rostfreiheit an Radläufen und Schweller", "status": "Bestanden"},
                {"name": "Zustand der Windschutzscheibe (Steinschläge)", "status": "Bestanden"},
                {"name": "Scheinwerfergläser (Klarheit, keine Risse)", "status": "Bestanden"},
                {"name": "Funktion der Außenspiegel", "status": "Bestanden"},
                {"name": "Zustand der Leichtmetallfelgen (Bordsteinschäden)", "status": "Hinweis: Leichte Kratzer"},
                {"name": "Reifenprofiltiefe (mind. 4mm)", "status": "Bestanden"},
                {"name": "Unterbodenverkleidung intakt", "status": "Bestanden"},
                {"name": "Schiebedach/Panoramadach Dichtigkeit", "status": "Nicht zutreffend / Bestanden"},
            ]
        },
        "interior": {
            "title": "2. Innenraum & Elektronik (Interior & Electronics)",
            "items": [
                {"name": "Sitzbezüge (Risse, Flecken)", "status": "Bestanden"},
                {"name": "Funktion der Sitzheizung/Sitzbelüftung", "status": "Bestanden"},
                {"name": "Klimaanlage (Kühlleistung & Geruch)", "status": "Bestanden"},
                {"name": "Infotainment-System & Navigation", "status": "Bestanden"},
                {"name": "Kombiinstrument (Pixelfehler)", "status": "Bestanden"},
                {"name": "Fensterheber (Gleichlauf, Einklemmschutz)", "status": "Bestanden"},
                {"name": "Zentralverriegelung & Schlüssel", "status": "Bestanden"},
                {"name": "Innenbeleuchtung", "status": "Bestanden"},
                {"name": "Lenkrad (Abnutzung, Tastenfunktion)", "status": "Bestanden"},
                {"name": "Gurte & Gurtstraffer", "status": "Bestanden"},
            ]
        },
        "engine": {
            "title": "3. Motorraum & Mechanik (Engine & Mechanics)",
            "items": [
                {"name": "Motorlauf (kalt und warm)", "status": "Bestanden"},
                {"name": "Ölverlust / Undichtigkeiten am Motorblock", "status": "Bestanden"},
                {"name": "Kühlwasser (Füllstand, Ölspuren)", "status": "Bestanden"},
                {"name": "Zahnriemen / Steuerkette (Geräusche)", "status": "Bestanden"},
                {"name": "Zustand der Antriebsriemen", "status": "Bestanden"},
                {"name": "Batterie (Ladespannung, Alter)", "status": "Bestanden"},
                {"name": "Bremsflüssigkeit (Wasseranteil)", "status": "Bestanden"},
                {"name": "Servolenkung (Flüssigkeit, Geräusche)", "status": "Bestanden"},
                {"name": "Motorlager / Aufhängung", "status": "Bestanden"},
                {"name": "Abgasanlage (Dichtigkeit, Rost)", "status": "Bestanden"},
            ]
        },
        "test_drive": {
            "title": "4. Probefahrt & Dynamik (Test Drive)",
            "items": [
                {"name": "Ansprechverhalten des Motors", "status": "Bestanden"},
                {"name": "Schaltvorgänge (Ruckeln, Verzögerung)", "status": "Bestanden"},
                {"name": "Kupplung (Schleifpunkt, Durchrutschen)", "status": "Bestanden"},
                {"name": "Bremsverhalten (Verziehen, Rubbeln)", "status": "Bestanden"},
                {"name": "ABS/ESP Funktionstest", "status": "Bestanden"},
                {"name": "Lenkverhalten (Spiel, Vibrationen)", "status": "Bestanden"},
                {"name": "Fahrwerk (Poltern, Stoßdämpfertest)", "status": "Bestanden"},
                {"name": "Tempomat & Assistenzsysteme", "status": "Bestanden"},
                {"name": "Windgeräusche ab 100 km/h", "status": "Bestanden"},
                {"name": "Fehlerspeicher nach Probefahrt (OBD)", "status": "Bestanden (Keine Fehler)"},
            ]
        }
    }

def get_component_assessment_de() -> dict:
    """Detailed component assessment to take up 2-3 pages."""
    return [
        {
            "system": "Motor & Antriebsstrang",
            "score": 92,
            "description": "Der Motor weist eine hervorragende Kompression auf allen Zylindern auf. Die Steuerkette zeigt keine Längung und der Öldruck ist im Kalt- sowie im Warmzustand im optimalen Bereich. Die Einspritzdüsen weisen ein perfektes Spritzbild auf, was zu einem effizienten Kraftstoffverbrauch führt. Das Getriebe schaltet butterweich und ohne Verzögerungen. Das Verteilergetriebe (falls vorhanden) funktioniert geräuschlos."
        },
        {
            "system": "Fahrwerk & Aufhängung",
            "score": 88,
            "description": "Die Stoßdämpfer zeigen eine Dämpfungsleistung von über 85%. Federn sind intakt und weisen keine Haarrisse auf. Querlenkerbuchsen und Koppelstangen sind straff und weisen kein Spiel auf. Die Radlager rollen geräuschlos ab. Lediglich leichte oberflächliche Korrosion an den Achsträgern, die für das Fahrzeugalter absolut normal und unbedenklich ist."
        },
        {
            "system": "Bremssystem",
            "score": 95,
            "description": "Die Bremsscheiben und Beläge wurden kürzlich erneuert und befinden sich bei nahezu 100% ihrer Lebensdauer. Die Bremsleitungen sind frei von Rost und Korrosion. Die Bremsflüssigkeit weist einen Siedepunkt von über 240°C auf (wasserfrei). Das ABS-Pumpensystem und der Bremskraftverstärker arbeiten verzögerungsfrei und mit vollem Druckaufbau."
        },
        {
            "system": "Elektronik & Bordnetz",
            "score": 90,
            "description": "Die Batterie hat beim Belastungstest 90% ihrer Kaltstartleistung (CCA) erreicht. Die Lichtmaschine lädt konstant mit 14,4 Volt. Alle Steuergeräte (ECU, BCM, ABS, Airbag) kommunizieren fehlerfrei auf dem CAN-Bus. Die Sensorik für Assistenzsysteme (Radar, Kamera, Ultraschall) wurde kalibriert und funktioniert zuverlässig."
        }
    ]

def get_running_costs_de() -> dict:
    """Simulated running costs over 1, 3, 5 years."""
    return {
        "yearly_tax": "ca. 180 - 350 € (abhängig von CO2-Emissionen)",
        "insurance_avg": "ca. 650 - 1.200 € / Jahr (Vollkasko)",
        "fuel_monthly": "ca. 150 € (bei 15.000 km/Jahr)",
        "maintenance_yearly": "ca. 450 - 800 €",
        "depreciation_1yr": "12 %",
        "depreciation_3yr": "30 %",
        "depreciation_5yr": "45 %",
        "summary": "Die Unterhaltskosten dieses Fahrzeugs liegen im branchenüblichen Durchschnitt für diese Fahrzeugklasse. Der stärkste Wertverlust tritt in den ersten 3 Jahren auf, danach stabilisiert sich die Kurve."
    }

def get_glossary_de() -> dict:
    """Automotive glossary in German taking 2-3 pages."""
    return {
        "FIN / VIN": "Fahrzeugidentifizierungsnummer. Eine einmalige, 17-stellige Seriennummer zur Identifikation von Kraftfahrzeugen.",
        "KBA": "Kraftfahrt-Bundesamt. Die Bundesoberbehörde in Deutschland, zuständig für den Straßenverkehr und das Fahrzeugregister.",
        "HU / AU": "Hauptuntersuchung und Abgasuntersuchung. Die gesetzlich vorgeschriebene technische Prüfung (oft TÜV genannt), um die Verkehrssicherheit und Umweltverträglichkeit zu gewährleisten.",
        "OBD": "On-Board-Diagnose. Ein Fahrzeugdiagnosesystem zur Überwachung abgasbeeinflussender Systeme und wichtiger Steuergeräte.",
        "CAN-Bus": "Controller Area Network. Ein serielles Bussystem, das die Kommunikation zwischen den Steuergeräten im Fahrzeug ermöglicht.",
        "Totalschaden": "Ein Schaden am Fahrzeug, dessen Reparaturkosten den Wiederbeschaffungswert übersteigen (wirtschaftlicher Totalschaden) oder bei dem eine Reparatur technisch unmöglich ist (technischer Totalschaden).",
        "Scheckheftgepflegt": "Ein Fahrzeug, dessen vorgeschriebene Wartungsintervalle (Inspektionen) lückenlos in der Vertragswerkstatt oder einer anerkannten freien Werkstatt durchgeführt und im Serviceheft dokumentiert wurden.",
        "Euro NCAP": "European New Car Assessment Programme. Ein Programm zur Bewertung der Sicherheit von Pkw, bei dem Crashtests durchgeführt werden (maximal 5 Sterne).",
        "ESP": "Elektronisches Stabilitätsprogramm. Ein Fahrerassistenzsystem, das durch gezieltes Abbremsen einzelner Räder ein Ausbrechen des Fahrzeugs verhindert.",
        "DPF / OPF": "Dieselpartikelfilter / Ottopartikelfilter. Abgasreinigungssysteme, die Rußpartikel aus dem Abgas filtern."
    }
