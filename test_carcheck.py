from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    
    print('Navigating to carcheck.co.uk...')
    page.goto('https://www.carcheck.co.uk/')
    page.wait_for_timeout(2000)
    
    try:
        page.fill('input[name="vrm"]', 'BK12KCG')
        page.locator('button[type="submit"]').first.click(timeout=3000)
        page.wait_for_timeout(5000)
        
        print('URL after search:', page.url)
        
        text = page.evaluate('document.body.innerText')
        for line in text.split('\n'):
            line = line.strip()
            if any(x in line.lower() for x in ['door', 'seat', 'tank', 'engine number', 'view', 'drivetrain', 'axle']):
                print('FOUND:', line)
                
    except Exception as e:
        print('Error:', e)
        
    browser.close()
