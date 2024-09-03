from playwright.async_api import async_playwright

async def check_assets_caching(url):

    class data(object): pass
    data.is_satisfied = False
    data.weight = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        print(url)
        page.on('response', lambda response: handle_response(response))

        try:
            await page.goto(url)
        except Exception as e:
            print(f"Error navigating to the URL: {e}")

        await context.close()
        await browser.close()

    return data

def handle_response(response):
   
    headers = response.headers
    cache_control = headers.get("Cache-Control", "")
    expires = headers.get("Expires", "")
    etag = headers.get("ETag", "")

    # Have to notify the user or save this data DB

    if "no-store" not in cache_control and not expires and not etag:
        print(f"Content not explicitly marked as not cacheable")
    else:
        print(f"Content may be cached")