from playwright.async_api import async_playwright

async def is_listed_on_google_business(website_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await  browser.new_context()
        page = await context.new_page()

        # Perform a Google search for the business name
        search_query = f"site:https://earnflex.com/ Google My Business"
        await page.goto(f"https://www.google.com/search?q={search_query}", timeout=60000)
        
        is_listed = False

        website_link_selector = ".yuRUbf a"  # Potentially more reliable selector
        if await page.query_selector(website_link_selector):
            is_listed = True

        # Additional check for explicit "Google My Business" text:
        google_business_selector = ".tF2Cxc"
        google_business_text = await page.inner_text(google_business_selector)
        if google_business_text.lower().strip() == "google my business":
            is_listed = True

        print(f"Website is{'' if is_listed else ' not'} listed in Google Business")
    
        await context.close()
        await browser.close()
