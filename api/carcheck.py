import httpx
from bs4 import BeautifulSoup

async def fetch_additional_info(registration: str) -> dict:
    """
    Fetch additional information (Engine Number, Doors, Seats, etc.)
    from carcheck.co.uk.
    Returns a dict with the extracted data, or None if extraction fails or data is missing.
    """
    reg = registration.upper().replace(" ", "")
    url = f"https://www.carcheck.co.uk/vrm/{reg}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, timeout=15.0)
            
        if resp.status_code != 200:
            return None
            
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        data = {}
        for tr in soup.find_all('tr'):
            th = tr.find('th')
            td = tr.find('td')
            if th and td:
                key = th.text.strip().lower()
                val = td.text.strip()
                if not val or val.lower() in ["n/a", "-", "unknown"]:
                    continue
                    
                if 'tank capacity' in key:
                    data['fuel_tank_capacity'] = val
                elif 'number of doors' in key:
                    data['number_of_doors'] = val
                elif 'number of seats' in key:
                    data['number_of_seats'] = val
                elif 'number of axles' in key:
                    data['number_of_axles'] = val
                elif 'engine number' in key:
                    data['engine_number'] = val
                elif 'drivetrain' in key or 'drive train' in key:
                    data['drivetrain'] = val
                elif 'steering position' in key:
                    data['steering_position'] = val
                    
        return data if data else None
        
    except Exception as e:
        print(f"Error fetching carcheck info for {reg}: {e}")
        return None
