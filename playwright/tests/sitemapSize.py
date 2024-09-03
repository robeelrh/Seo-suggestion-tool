import xml.etree.ElementTree as ET
from playwright.async_api import async_playwright

async def check_sitemap_size_and_links(url):

    class data(object): pass
    data.is_satisfied = False
    data.no_of_links = 0
    data.size = 0
    data.weight = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        sitemap_url = f"{url}sitemap.xml"
        response = await page.goto(sitemap_url)

        body = await response.body()
        data.size = len(body)
        
        content = await page.content()

        if '<urlset' in content:
            root = ET.fromstring(content)
            urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            data.no_of_links = len(urls)
        else:
            print(f"Sitemap not found.")

        if data.size < 40000000 and data.no_of_links < 40000:
            data.is_satisfied = True
            data.weight = 1

        await browser.close()

    return data


        

