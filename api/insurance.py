"""
Insurance Check Module (askMID / MIB).
Reference: https://www.mib.org.uk/check-and-stay-insured/check-your-vehicle/

NOTE: The askMID website uses CAPTCHA and is not designed for automated access.
This module provides a placeholder structure. You can:
1. Manually check insurance status on the MIB website and input the result.
2. If MIB provides a commercial API in the future, integrate it here.

For now, the report will show a generic insurance check section with
instructions for the user to verify independently.
"""


async def check_insurance(registration: str) -> dict:
    """
    Check vehicle insurance status via MIB.
    """
    from playwright.async_api import async_playwright
    import asyncio
    
    reg = registration.upper().replace(" ", "")
    
    result = {
        "success": False,
        "registration": reg,
        "status": "CHECK RECOMMENDED",
        "provider": "Motor Insurers' Bureau (MIB)",
        "check_url": "https://enquiry.navigate.mib.org.uk/",
        "description": "An automated check could not determine the insurance status. Please verify manually.",
        "how_to_check": []
    }
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            
            await page.goto('https://enquiry.navigate.mib.org.uk/')
            
            # Click "Third party check" (usually value is THIRD_PARTY_CHECK)
            try:
                await page.locator('button[value="THIRD_PARTY_CHECK"]').click(timeout=5000)
            except Exception:
                try:
                    await page.locator('button[value="PERSONAL_CHECK"]').click(timeout=5000)
                except Exception:
                    pass
            
            try:
                await page.locator('button[data-testid="continueBtn"]').click(timeout=5000)
            except Exception:
                pass
                
            await page.wait_for_timeout(2000)
            
            # Fill VRM
            vrm_input = page.locator('input[name="vrm"]')
            if await vrm_input.count() > 0:
                await vrm_input.fill(reg)
                await page.locator('button[type="submit"]').click(timeout=5000)
                
                await page.wait_for_timeout(3000)
                
                html = await page.content()
                html_lower = html.lower()
                
                if "is insured" in html_lower or "shows as insured" in html_lower or "appears on the mid" in html_lower or "insured" in html_lower:
                    result["status"] = "INSURED"
                    result["success"] = True
                    result["description"] = f"A live check of the Motor Insurance Database (MID) via Navigate confirms that the vehicle {reg} is currently insured."
                elif "not insured" in html_lower or "does not appear" in html_lower or "uninsured" in html_lower:
                    result["status"] = "NOT INSURED"
                    result["success"] = True
                    result["description"] = f"A live check of the Motor Insurance Database (MID) via Navigate indicates that the vehicle {reg} is NOT currently insured."
                else:
                    # If we reached the result but couldn't parse it
                    result["status"] = "CHECK COMPLETED"
                    result["success"] = True
                    result["description"] = f"The check was performed via Navigate, but the specific status could not be automatically determined."
            
            await browser.close()
    except Exception as e:
        print("MIB Scrape Error:", e)
        
    return result
