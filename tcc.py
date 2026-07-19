from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://totalcarcheck.co.uk/FreeCheck?regno=BK12KCG')
        page.wait_for_timeout(3000)
        
        try:
            page.click('a[href="#mot"]', timeout=3000)
            page.wait_for_timeout(1000)
        except Exception as e:
            pass
            
        with open('tcc_html.txt', 'w', encoding='utf-8') as f:
            f.write(page.content())
        print('Saved to tcc_html.txt')
        browser.close()
test()
