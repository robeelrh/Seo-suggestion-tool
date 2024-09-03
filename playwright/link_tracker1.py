import requests, time, random, os
from requests.exceptions import InvalidSchema
from urllib.parse import urljoin
from dotenv import load_dotenv

# Initialize global variables
active_links = []
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
cookies = {'cookie_name': 'cookie_value'}

def link_validator(url, trigger_url):
    """
    Validates the given URL and determines if it is an outgoing link.
    Efficiently handles different URL patterns and sets the outgoing flag accordingly.
    """
    out_going = False

    if url.startswith("/") and len(url) > 1:
        url = trigger_url + url[1:]
    elif url in ["/", "/#"]:
        url = None
    elif url.startswith("#"):
        url = trigger_url + url[1:]
    elif not url.startswith(trigger_url):
        out_going = True

    return url, out_going

async def check_sub_links(link_that_is_being_crawled, page, trigger_url, depth):
    global active_links

    for link in await page.query_selector_all('a'):
        href = await link.get_attribute('href')

        if href:
            valid_link, out_going = link_validator(href, trigger_url)
            if valid_link and not out_going:
                link_found = False
                for item in active_links:
                    if valid_link == item["url"]:
                        link_found = True
                        break

                if not link_found:
                    print(f'\nHitting this URL (total count {len(active_links)}): {valid_link}\n')
                    if random.uniform(0, 2) > 1:  # Random sleep to simulate variable processing time
                        time.sleep(random.uniform(0, 1))
                    try:
                        response = requests.head(valid_link, headers=headers, cookies=cookies)
                        redirected_URL = ''
                        if response.status_code == 301:
                            print(f'\nRedirection Detected | Notify the user!\n')
                            redirected_URL = response.headers.get('Location')

                        # Include depth information here
                        active_links.append({"url": valid_link, 'status_code': response.status_code, 'out_going': out_going, 'redirected_URL': redirected_URL, 'depth': depth + 1})
                    except InvalidSchema as e:
                        print(f"Error: {e}")
                # else:
                #     print(f'Duplicate / Invalid Link: {valid_link}')

    return list(active_links)
