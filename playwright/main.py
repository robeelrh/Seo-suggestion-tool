
import os
import asyncio
import argparse
from datetime import datetime
from link_tracker import check_sub_links
from tests import robotTxt
from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
from playwright.async_api import async_playwright,  TimeoutError as PlaywrightTimeoutError

submited_links = []
total_links = []
max_pages = 0
domain_url = ''
time_stamp = ''
scraper_id = 0
resgistered_scrapers = []

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
}

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

async def fetch_links(input_params, sleep_time):

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for index, item in enumerate(input_params):
            url = item["url"]

            if item["out_going"] == False:

                # print(f'\nProcessing link at index {index}/{len(input_params)}: {url}')
                page = await browser.new_page()
                # page.on('response', lambda response: check_for_redirections(response))
                await page.goto(url)

                # Passsing 'url' parameter here because we have to get all the links for this specific url. HINT: urls_urls
                sub_links = await check_sub_links(url, page, domain_url, input_params, sleep_time)
                total_links.extend(sub_links)

                # Merge sub_links into input_params while keeping it unique
                unique_sub_links = [sub_link for sub_link in sub_links if sub_link not in input_params]
                input_params.extend(unique_sub_links)
                submited_links.extend(unique_sub_links)

                print(f'\nLinks from child function: {len(submited_links)}\n')
                await page.close()

                if len(submited_links) >= 10:
                    links_to_submit = submited_links[:10]

                    if len(total_links) >= max_pages:
                        await submitLinks(links_to_submit, 'final_iteration')
                    else:
                        await submitLinks(links_to_submit, 'running')
                        submited_links = submited_links[10:]

    await browser.close()
    return input_params

async def getDomainFromProjectId(id):
    global time_stamp, max_pages
    response = requests.post(f'{BASE_URL}/api/project/get', json={"project_id": id}, headers=headers)

    data = response.json()
    print(f"\nProject Data: {response.json()}")

    max_pages = data[0]["max_pages_to_crawl"]
    time_stamp = data[0]["created_at"]
    result = await robotTxt.check_robots_txt(data[0]['url'])

    if result.is_satisfied:
        return data[0]
    else:
        print('Crawler is not allowed on this page')

async def getDomainFromScraperId(id):
    response = requests.post(f'{BASE_URL}/api/scrapers/get_by_id', json={"scraper_id": id}, headers=headers)
    data = response.json()
    print(f"{data}")
    return data[0]
    result = await robotTxt.check_robots_txt(data[0]['domain_url'])

    if result.is_satisfied:
        return data[0]
    else:
        print('Crawler is not allowed on this page')

async def main(project_id_param):
    global max_pages, total_links, domain_url, submited_links, project_id, scraper_id, resgistered_scrapers, submited_links, total_links

    data = await getDomainFromProjectId(project_id_param)
    # data = await getDomainFromScraperId(args.scraper_id)

    # Need to start scraper session from here:
    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    scraper_payload = {
        'domain_url': data['url'],
        'project_id': int(project_id_param),
        'tracing': False,
        'follow_links': False,
        'sleep_time': int(data['crawler_speed']),
        'status': 'pending',
        'started_at': datetime_string,
        'follow_index': 0,
        'follow_noindex': 0,
        'nofollow_index': 0,
        'nofollow_noindex': 0,
        'no_meta_no_robots': 0,
        'ended_at': '',
    }
    scraper_response = requests.post(f'{BASE_URL}/api/scrapers/create', json= scraper_payload, headers=headers)
    scraper_data = scraper_response.json()

    print(f"Scraper Registeration: {scraper_response.json()}")
    scraper_id = scraper_data["id"]

    domain_url = await normalize_url(data['url'])

    sitemap = get_sitemap_links(domain_url)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        page.on('response', lambda response: check_for_redirections(response))

        await page.goto(data['url'])
        # await page.goto("https://wemasy.nl/test_redirection")

        # Passsing 'data['url']' parameter here because we have to get all the links for this specific url. HINT: urls_urls

        active_links = await check_sub_links(data['url'], page, domain_url, total_links, int(data['crawler_speed']))
        total_links.extend(active_links)
        await browser.close()

        if len(total_links) >= max_pages:
            await submitLinks(active_links, 'final_iteration')
            return

        submited_links = active_links

        # if scraper_response["follow_links"]:
        #     all_links = await fetch_links(active_links, int(data['crawler_speed']))

        if len(submited_links) > 0:
            await submitLinks(submited_links, 'final_iteration')

async def submitLinks(links, flag):
    update_scraper_url = f"{BASE_URL}/api/scrapers/update_scraper"

    if flag == 'final_iteration':
        current_datetime = datetime.now()
        datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        update_scraper_payload = {
            "scraper_id": int(scraper_id),
            "status": 'completed',
            "ended_at": datetime_string
        }

        # Need to get whole websites data for: follow_index, follow_noindex, nofollow_index, nofollow_noindex, no_meta_no_robots
        await getMetaInfoAndUpdate()

    else:
        update_scraper_payload = {
            "scraper_id": int(scraper_id),
            "status": 'progress',
        }

    # Need to update the status flag and ended_time of the scraper session
    update_scraper_response = requests.post(update_scraper_url, json=update_scraper_payload, headers=headers)
    print(f"Update scraper response 1: {update_scraper_response.json()}")
    if update_scraper_response.status_code == 201 or update_scraper_response.status_code == 200:
        print("API call successfull")
    else:
        print(f"API call failed with status code {update_scraper_response.status_code}")


    payload = {
        "scraper_id": int(scraper_id),
        "urls": links,
        "redirected_URL": ''
    }

    response = requests.post(f"{BASE_URL}/api/scrapers/urls/create", json=payload, headers=headers)
    scrapers_data = response.json()
    resgistered_scrapers.extend(scrapers_data["resgistered_scrapers"])

    if len(resgistered_scrapers) > 0:
        await getTracersAndSiteMapData()

    if response.status_code == 201 or response.status_code == 200:
        print("API call successful")
    else:
        print(f"API call failed with status code {response.status_code}")

async def normalize_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        domain_url = parsed_url.scheme+'://'+parsed_url.netloc+'/'
    elif url.startswith('www.'):
        domain_url = 'https://'+url+'/'
    else:
        domain_url = None

    return domain_url

async def getTracersAndSiteMapData():
    for scraper in resgistered_scrapers:
        if not scraper["out_going"]:

            sitemap_data_payload = {
                'scraped_url_id': int(scraper["id"]),
                'scraped_url': scraper["scraped_url"],
                'site_map_content': ''
            }

            robotTxt_url = scraper["scraped_url"].rstrip('/') + '/robots.txt'
            response = requests.get(robotTxt_url)

            content = []

            if response.status_code == 200:
                sitemap_data_payload["site_map_content"] = response.text

                if response.text.lower().startswith("user-agent"):
                    for line in response.text.splitlines():
                        content.append(line)

            sitemap_data_payload["site_map_content"] = str(content)
            response = requests.post(f"{BASE_URL}/api/scraped_url/create_sitemap_data", json=sitemap_data_payload, headers=headers)
            sitemap_data_response = response.json()

        async with async_playwright() as p:
            browser = await p.chromium.launch()  # headless = False
            context = await browser.new_context(user_agent='WEMASY CRAWLING')

            await context.tracing.start(name="trace", screenshots=True, snapshots=True)
            page = await context.new_page()

            try:
                # Setting a timeout of 30 seconds for the page.goto() function
                await page.goto(scraper["scraped_url"], timeout=30000)
                # Additional page interactions go here
            except PlaywrightTimeoutError:
                print(f"Timeout occurred while trying to access {scraper['scraped_url']}")
            finally:
                await context.tracing.stop(path=f"{scraper['id']}.zip")

            await browser.close()


async def getMetaInfoAndUpdate():

     # Initialize counters
    seo_categories = {
        'follow_index': 0,
        'follow_noindex': 0,
        'nofollow_index': 0,
        'nofollow_noindex': 0,
        'no_meta_no_robots': 0
    }

    for link in total_links:
        if not link["out_going"]:
            # print(f"\nLINK---------{link["url"]}\n")

            # Getting data for scraper for get all these paramters:
            # follow_index, follow_noindex, nofollow_index, nofollow_noindex, no_meta_no_robots

            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(link["url"])
                links = await page.query_selector_all('a')

                # Check for meta robots
                meta_robots = await page.content()
                noindex = 'noindex' in meta_robots
                has_meta_robots = '<meta name="robots"' in meta_robots or 'content="noindex"' in meta_robots

                for link in links:
                    rel = await link.get_attribute('rel')
                    nofollow = 'nofollow' in rel if rel else False

                    # Determine category
                    if not has_meta_robots:
                        seo_categories['no_meta_no_robots'] += 1
                    elif nofollow and noindex:
                        seo_categories['nofollow_noindex'] += 1
                    elif nofollow and not noindex:
                        seo_categories['nofollow_index'] += 1
                    elif not nofollow and noindex:
                        seo_categories['follow_noindex'] += 1
                    elif not nofollow and not noindex:
                        seo_categories['follow_index'] += 1

                await browser.close()
                print(f'Updated Scraper: {seo_categories}')

    update_scraper_url = f"{BASE_URL}/api/scrapers/update_scraper"
    update_scraper_payload = {
        "scraper_id": int(scraper_id),
        "follow_index": seo_categories['follow_index'],
        "follow_noindex": seo_categories['follow_noindex'],
        "nofollow_index": seo_categories['nofollow_index'],
        "nofollow_noindex": seo_categories['nofollow_noindex'],
        "no_meta_no_robots": seo_categories['no_meta_no_robots']
    }

    update_scraper_response = requests.post(update_scraper_url, json=update_scraper_payload, headers=headers)
    print(f"Update scraper response 2: {update_scraper_response.json()}")
    if update_scraper_response.status_code == 201 or update_scraper_response.status_code == 200:
        print("API call successful")
    else:
        print(f"API call failed with status code {update_scraper_response.status_code}")


def check_for_redirections(response):
    # Check if there is a status code indicating redirection
    if response.status == 301 or response.status == 302:
        print("There is a redirection")

def get_sitemap_links(url):
    for sitemap_url in ["sitemap.xml", "sitemap_index.xml"]:
        response = requests.get(url + sitemap_url)
        if response.status_code == 200:
            return url + sitemap_url

async def tester():
    robotTxt_url = 'https://wemasy.nl' + '/robots.txt'
    print(f"\n{robotTxt_url}\n")
    response = requests.get(robotTxt_url)

    if response.status_code == 200:
        for line in response.text.splitlines():
            print(f'\nSitemap ------- {line}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id')
    # parser.add_argument('--scraper_id')

    args = parser.parse_args()
    print(f"{args.project_id}")
    asyncio.run(main(args.project_id))
    # asyncio.run(tester())
