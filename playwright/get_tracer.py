from playwright.async_api import async_playwright
import argparse
import requests
import asyncio

parser = argparse.ArgumentParser()
parser.add_argument('--scraped_url_id', type=str)

args = parser.parse_args()
domain_url = ''
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
}

async def main():
    domain_url = await getDomainFromScrapedUrlId(args.scraped_url_id)
    await getTracer(domain_url)

async def getDomainFromScrapedUrlId(id):
    response = requests.post('http://127.0.0.1:8000/api/scrapers/urls/get_scraped_url', json={"scraped_url_id": id}, headers=headers)
    data = response.json()
    print(data)
    return data[0]['scraped_url']

async def getTracer(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(user_agent = 'WEMASY CRAWLING')
        
        await context.tracing.start(name="trace", screenshots=True, snapshots=True)
        page = await context.new_page()
        await page.goto(url)
        await context.tracing.stop(path = f"{args.scraped_url_id}.zip")
        
        response = requests.head(url, headers=headers)
        print({"url": url, 'status_code': response.status_code})

        await context.close()
        await browser.close()
        
if __name__ == '__main__':
    asyncio.run(main())
