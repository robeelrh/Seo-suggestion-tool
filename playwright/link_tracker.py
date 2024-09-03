import requests
import time
import random
import os
import argparse
from requests.exceptions import InvalidSchema, Timeout, SSLError
from urllib.parse import urljoin
from dotenv import load_dotenv

parent_child_links = []
active_links = []
url_urls = []
on_going_url = ''
scraper_id = 0

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
cookies = {'cookie_name': 'cookie_value'}

def link_validator(url, trigger_url):
    out_going = False

    if url.startswith("/") and len(url) >= 1:
        url = trigger_url + url[1:]
    elif url == "/" and len(url) > 1:
        url = None
    elif url.startswith("/#") and len(url) > 1:
        url = None
    elif url.startswith("#") and len(url) >= 1:
        url = trigger_url + url[1:]
    elif not url.startswith(trigger_url):
        out_going = True

    return url, out_going

async def check_sub_links(link_that_is_being_crawled, page, trigger_url, input_array, sleep_time):
    global url_urls, scraper_id, on_going_url, active_links, parent_child_links, indexed_flad

    for link in await page.query_selector_all('a'):
        href = await link.get_attribute('href')

        if href:
            valid_link, out_going = link_validator(href, trigger_url)
            if valid_link:

                indexed_flad = False
                if not out_going:
                    try:
                        robots_url = valid_link.rstrip('/') + '/robots.txt'
                        indexed_response = requests.get(robots_url)
                        indexed_flad = indexed_response.status_code == 200

                    except InvalidSchema as e:
                        print(f"Error occurred while fetching robots.txt for {valid_link}: {e}")
                        indexed_flad = False

                link_found = False
                for item in active_links:
                    if valid_link == item["url"]:
                        link_found = True
                        break

                if not link_found and  "twitter" not in valid_link:
                    print(f'Hitting this URL (total count {len(active_links)}): {valid_link}')
                    if sleep_time is not None:
                        time.sleep(random.uniform(0, sleep_time))
                    try:
                        response = requests.head(valid_link, headers=headers, cookies=cookies, verify=False)
                        redirected_URL = ''
                        if response.status_code == 301:
                            print(f'\nRedirection Detected | Notify the user!\n')

                            if valid_link.startswith('https'):
                                redirected_URL = response.headers.get('Location')
                            else:
                                print(f'\nRedirection link is HTTP\n')

                        active_links.append({"url": valid_link, 'status_code': response.status_code, 'out_going': out_going, 'redirected_URL': redirected_URL, 'indexed': indexed_flad})

                    except (SSLError, Timeout) as e:
                        print(f"Error: {e}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print(f'Duplicate / Invalid Link: {valid_link}')

    return list(active_links)
