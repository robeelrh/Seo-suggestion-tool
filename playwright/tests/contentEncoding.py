from playwright.async_api import async_playwright

async def check_content_encoding(url):
    
    class data(object): pass
    data.is_satisfied = False
    data.is_content_encoding = False
    data.weight = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        response = await page.goto(url)
        
        content_encoding = response.headers.get("Content-Encoding")

        if content_encoding:
            data.is_satisfied = True
            data.is_content_encoding = True
            data.weight = 1
        
    return data     