import asyncio
from playwright.async_api import async_playwright

async def test_askmid():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to askmid...")
        await page.goto('https://ownvehicle.askmid.com/')
        print("Filling form...")
        await page.fill('input[name="RegistrationNumber"]', 'BK12KCG')
        await page.check('input[name="DeclarationConsent"]')
        await page.click('button[type="submit"]')
        print("Waiting...")
        await page.wait_for_timeout(3000)
        
        html = (await page.content()).lower()
        if 'is showing as insured' in html or 'is insured' in html:
            print('INSURED')
        elif 'is not showing as insured' in html or 'not insured' in html:
            print('NOT INSURED')
        else:
            print('UNKNOWN')
            print(html[:1000])
        await browser.close()

asyncio.run(test_askmid())
