from link_tracker1 import check_sub_links
from playwright.async_api import async_playwright
import asyncio
import os

submited_links = []  # Tracks links that have been processed
total_links = []  # All discovered links
domain_url = 'https://wemasy.nl/'  # Set your domain URL here

async def fetch_links(start_url, max_depth):
    global submited_links, total_links
    depth = 0  # Starting depth
    to_crawl = [{'url': start_url, 'depth': depth}]  # Queue of URLs to crawl with their depths

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        while to_crawl:
            current = to_crawl.pop(0)  # Get the next URL and its depth
            url, depth = current['url'], current['depth']

            if url not in submited_links:
                print(f"Crawling: {url} at depth {depth}")
                page = await browser.new_page()
                await page.goto(url)
                submited_links.append(url)  # Mark this URL as processed

                # Fetch sub-links from the current URL, incrementing the depth
                sub_links = await check_sub_links(url, page, domain_url, depth)
                
                # Filter out already submitted or to be crawled links to avoid duplication
                
                # new_links = [link for link in sub_links if link['url'] not in submited_links and not already_in_queue(to_crawl, link['url'])]
                new_links = [link for link in sub_links if link['url'] not in submited_links]

                to_crawl.extend(new_links)  # Add new links to the crawl queue
                total_links.extend(new_links)
                await page.close()

        await browser.close()

def already_in_queue(queue, url):
    """Check if a URL is already in the crawling queue."""
    return any(item['url'] == url for item in queue)

async def main():
    start_url = 'https://wemasy.nl/'
    max_depth = 2
    await fetch_links(start_url, max_depth)

    # print(f"-----All Links: \n {total_links} \n------")

if __name__ == '__main__':
    asyncio.run(main())
