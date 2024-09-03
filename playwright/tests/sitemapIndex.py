import xml.etree.ElementTree as ET
from playwright.async_api import async_playwright

async def check_noindex_in_sitemap(url):

    class data(object): pass
    data.is_satisfied = False
    data.noindex_urls = []
    data.weight = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        sitemap_url = f"{url}/sitemap.xml"
        response = await page.goto(sitemap_url)

        if response.status == 200:
            content = await page.content()
            if '<urlset' in content:
                root = ET.fromstring(content)
                urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
                
                for url in urls:
                    page_response = await page.goto(url)
                    if page_response.status == 200:
                        page_content = await page.content()
                        if '<meta name="robots" content="noindex"' in page_content.lower() or '<meta content="noindex" name="robots"' in page_content.lower():
                            data.is_satisfied = True
                            data.weight = 1
                            data.noindex_urls.append(url)
                            print(f"No index array: {data.noindex_urls}")
            else:
                print("Sitemap not found.")
        else:
            print("Failed to fetch sitemap.")

        print(f"No index array: {data.noindex_urls}")
        await browser.close()

    return data