from playwright.async_api import async_playwright
from dotenv import load_dotenv

import os
import asyncio
import requests
import argparse

parent_child_links = []
submited_links = []
total_links = []
domain_url = ''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
}

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

async def getScrapedUrlInfo(id):
    response = requests.post(f'{BASE_URL}/api/scraped_url/get_by_id', json={"scraped_url_id": id}, headers=headers)
    data = response.json()
    print(f"{data}")
    return data

async def main():
    global parent_child_links
    data = await getScrapedUrlInfo(args.scraped_url_id)
    
    path_segments = data[0]['scraped_url'].split('/')
    print(f"{path_segments}")


    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(data[0]['scraped_url'])

        for link in await page.query_selector_all('a'):
            href = await link.get_attribute('href')
            # print(f"{href}")

            if href:
                if href.startswith("/"):
                    print(f"{href}")
                    href = f"{path_segments[0]}//{path_segments[2]}{href}"
            
                    parent_child_links.append(href)
        # print(f"{parent_child_links}")
        await submitLinks(parent_child_links)
        await browser.close()

async def submitLinks(links):
    # print(f'\nLinks: {links}\n')
    url = f"{BASE_URL}/api/scrapers/urls_urls/create"
    payload = {
        "scraped_url_id": int(args.scraped_url_id),
        "urls": links
    }
    
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    if response.status_code == 201 or response.status_code == 200:
        print("API call successful")
    else:
        print(f"API call failed with status code {response.status_code}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scraped_url_id')
    args = parser.parse_args()
    asyncio.run(main())
