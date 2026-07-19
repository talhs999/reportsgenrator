from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.gov.uk/check-mot-history')
        page.click('a:has-text("Start now")')
        page.wait_for_timeout(2000)
        print("URL:", page.url)
        print(page.content()[:1000])
        browser.close()
test()
