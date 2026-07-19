import asyncio
from playwright.async_api import async_playwright

async def check_site(p, name, url, reg_selector, btn_selector, reg='YK19XNA'):
    try:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print(f"[{name}] Navigating...")
        await page.goto(url, timeout=15000)
        
        # Handle cookie banners blindly if they exist
        try:
            await page.click('button:has-text("Accept")', timeout=2000)
        except:
            pass
        try:
            await page.click('button:has-text("Agree")', timeout=2000)
        except:
            pass

        if 'totalcarcheck' not in name:
            await page.fill(reg_selector, reg)
            await page.click(btn_selector)
        await page.wait_for_timeout(5000)
        title = await page.title()
        content = await page.content()
        print(f'[OK] {name}: {title} | Size: {len(content)}')
    except Exception as e:
        print(f'[FAIL] {name}: {e}')
    finally:
        await browser.close()

async def run():
    async with async_playwright() as p:
        tasks = [
            check_site(p, 'vehiclescore', 'https://vehiclescore.co.uk/', 'input[name="vrm"]', 'button[type="submit"]'),
            check_site(p, 'motorscan', 'https://motorscan.co.uk/', 'input[name="vrm"]', 'button[type="submit"]'),
            check_site(p, 'totalcarcheck', 'https://totalcarcheck.co.uk/FreeCheck?regNo=YK19XNA', 'input[name="vrm"]', 'button[type="submit"]')
        ]
        await asyncio.gather(*tasks)

asyncio.run(run())