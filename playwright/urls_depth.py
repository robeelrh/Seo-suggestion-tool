from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from collections import deque

def is_same_domain(url1, url2):
    return urlparse(url1).netloc == urlparse(url2).netloc

def crawl_website_depth(homepage, target_url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        visited = set()
        queue = deque([(homepage, 0)])  # (URL, depth)
        url_depth = {}

        while queue:
            current_url, depth = queue.popleft()
            if current_url in visited:
                continue
            visited.add(current_url)
            url_depth[current_url] = depth

            # Stop if we've found the target URL
            if current_url == target_url:
                break

            page.goto(current_url)
            links = page.query_selector_all("a")
            for link in links:
                href = link.get_attribute("href")
                if href and is_same_domain(href, homepage):
                    absolute_url = urljoin(current_url, href)
                    if absolute_url not in visited:
                        queue.append((absolute_url, depth + 1))

        browser.close()
        return url_depth.get(target_url)

# Usage
homepage = "https://wemasy.nl/"
target_url = "https://wemasy.nl/bilal1/bilal2"
depth = crawl_website_depth(homepage, target_url)
print(f"Depth of {target_url} from {homepage} is: {depth}")
