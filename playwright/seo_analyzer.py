from playwright.async_api import async_playwright
from file_unzip import extract_html_file, extract_network_content, extract_ssl_details, extract_words_from_body, check_file_size
import argparse
import requests
import asyncio
import re
import bs4
import os
import zipfile
from datetime import datetime
from dotenv import load_dotenv

from tests import favicon, titleTag, metaDescription, headerTag, imgTagsSizeDim, robotTxt, urlFormat, keywordOptimization, metaTags, httpLinks, doctype, iframes, urlLength, metaEncoding, contentEncoding, breadcrumb, resourcesCompression, canonicalURL, assetsCaching, googleListing, testOpenGraphProtocol, sitemapSize, sitemapIndex, pageContent

import suggestions.breadcrumb.main as suggestion_breadcrumb
import suggestions.doctype.main as suggestion_doctype
import suggestions.favicon.main as suggestion_favicon
import suggestions.http_link.main as suggestion_http_link
import suggestions.iframe_count.main as suggestion_iframe_count
import suggestions.image_tags_size_dimensions.main as suggestion_image_tags_size_dimensions
import suggestions.keyword_optimization.main as suggestion_keyword_optimization
import suggestions.meta_description.main as suggestion_meta_description
import suggestions.meta_encoding.main as suggestion_meta_encoding
import suggestions.open_graph_protocols.main as suggestion_open_graph_protocols
import suggestions.page_content.main as suggestion_page_content
import suggestions.site_map_size.main as suggestion_site_map_size
import suggestions.title_tag.main as suggestion_title_tag

parser = argparse.ArgumentParser()
parser.add_argument('--scraped_url_id', type=str)
parser.add_argument('--pKeyword', type=str)

args = parser.parse_args()
domain_url = ''
seo_configurations = {}

base_path = os.getcwd()

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
}

payload = {
    "scraped_url_id": int(args.scraped_url_id),
    "scraper_id": 0,
    "url": "",
    "data": {}
}

async def main():
    global payload, base_path, domain_url
    await getSeoConfig()
    data = await getDomainFromScrapedUrlId(args.scraped_url_id)
    payload['url'] = data['scraped_url']
    payload['scraper_id'] = data['scraper_id']
    domain_url = data['scraped_url']
    
    await trigger_tests(domain_url, '')

async def getSeoConfig():
    global seo_configurations
    response = requests.post(f'{BASE_URL}/api/seo_configuration/get', json={"seo_config_id": 1})
    seo_configurations = response.json()

async def getDomainFromScrapedUrlId(id):
    response = requests.post(f'{BASE_URL}/api/scrapers/urls/get_scraped_url', json={"scraped_url_id": id}, headers=headers)
    data = response.json()
    return data[0]


def get_suggestion(result, label):
    suggestion_param = {}
    result_dict = result.__dict__

    if label == "favicons":
        keys = ["is_satisfied", "favicon"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_favicon.main(suggestion_param["favicon"], suggestion_param["is_satisfied"])

    elif label == "title_tags":
        keys = ["is_satisfied", "title_len"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_title_tag.main(suggestion_param["title_len"], suggestion_param["is_satisfied"])

    elif label == "meta_descriptions":
        keys = ["is_satisfied", "description_length"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_meta_description.main(suggestion_param["description_length"], suggestion_param["is_satisfied"])

    elif label == "keyword_optimizations":
        keys = ["is_satisfied", "is_secondary_satisfied", "is_primary_satisfied", "primary_count"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_keyword_optimization.main(
            suggestion_param["primary_count"], 
            suggestion_param["is_primary_satisfied"], 
            suggestion_param["is_secondary_satisfied"], 
            suggestion_param["is_satisfied"]
        )

    elif label == "img_tags_size_dims":
        keys = ["is_alt_satisfied", "is_size_satisfied", "is_dimension_satisfied", "is_satisfied"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_image_tags_size_dimensions.main(
            suggestion_param["is_alt_satisfied"], 
            suggestion_param["is_size_satisfied"], 
            suggestion_param["is_dimension_satisfied"], 
            suggestion_param["is_satisfied"]
        )

    elif label == "header_tags":
        return "No suggestion so far"

    elif label == "meta_tags":
        return "No suggestion so far"

    elif label == "sitemap_size_and_links":
        keys = ["is_satisfied", "no_of_links", "size"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_site_map_size.main(
            suggestion_param["no_of_links"], 
            suggestion_param["size"], 
            suggestion_param["is_satisfied"]
        )

    elif label == "check_page_content":
        keys = ["is_empty", "content_len"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_page_content.main(suggestion_param["content_len"], suggestion_param["is_empty"])

    elif label == "http_links":
        keys = ["is_satisfied", "http_satisfied", "https_satisfied"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_http_link.main(
            suggestion_param["http_satisfied"], 
            suggestion_param["https_satisfied"], 
            suggestion_param["is_satisfied"]
        )

    elif label == "doc_type":
        keys = ["is_satisfied", "doctype"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_doctype.main(suggestion_param["doctype"], suggestion_param["is_satisfied"])

    elif label == "iframes_count":
        keys = ["is_satisfied", "iframes_count"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_iframe_count.main(suggestion_param["iframes_count"], suggestion_param["is_satisfied"])

    elif label == "meta_encoding":
        keys = ["meta_encoding", "is_satisfied"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        return suggestion_meta_encoding.main(suggestion_param["meta_encoding"], suggestion_param["is_satisfied"])

    elif label == "resources_compression":
        return "No suggestion so far"

    elif label == 'og_meta_content':
        keys = ["is_satisfied"]
        suggestion_param = {key: result_dict.get(key) for key in keys}
        suggestion_param.update({
            "og_image": True,
            "og_type": True,
            "og_title": True,
            "og_description": True,
            "og_locale": True
        })
        return suggestion_open_graph_protocols.main(
            suggestion_param["og_image"], 
            suggestion_param["og_type"], 
            suggestion_param["og_title"], 
            suggestion_param["og_description"], 
            suggestion_param["og_locale"], 
            suggestion_param["is_satisfied"]
        )

    return "No suggestion so far"




async def run_and_append_test(page, test_function, label, payload):
    if label == 'header_tags':
        result = await test_function(page, '', seo_configurations)
    elif label == 'meta_tags':
        result = await test_function(page, seo_configurations)
    elif label == 'sitemap_size_and_links' or label == 'sitemap_indexing':
        result = await test_function(domain_url)
    elif label == 'keyword_optimizations':
        result = await test_function(page, '')
    # elif label == 'url_formats' or label == 'url_length' or label == 'content_encoding' or label == 'assets_caching':
    #     result = await test_function(domain_url)
    else:
        result = await test_function(page)
        
    check_result = {}
    for key, value in result.__dict__.items():
        if key.startswith("__"):
            continue
        check_result[key] = value
        payloadObj = {
            label: check_result
        }
    
    check_result["suggestion"] = get_suggestion(result, label)
    print("check_result: ", check_result)
    payload["data"][label] = check_result



async def get_content_percentage(html_path):
    with open(html_path, "r") as html:
        content = bs4.BeautifulSoup(html, "html.parser")
        text = content.get_text(separator="\n", strip=True)
        return len(text)

async def get_primaryKeyword_percentage(html_path, primaryKeyword):
    count = 0
    with open(html_path, "r") as html:
        content = bs4.BeautifulSoup(html, "html.parser")
        for h1_tag in content.find_all("h1"):
            h1_tag.extract()
        text = content.get_text(separator="\n", strip=True)
        lines = text.splitlines()
        for key in lines:
            if primaryKeyword != '' and primaryKeyword in key:
                count += 1
        return round((count/len(lines))*100, 4)

async def loadTraceFilesForSeoTest():
    
    if os.path.exists(f"{base_path}/extracted/scrapedUrlId_{args.scraped_url_id}"):
       print(f"File exists")
       return True
    else:

        if os.path.exists(f"{args.scraped_url_id}.zip"):
            print(f"Zip File exists")

            extractedPath = f"{base_path}/extracted/"
            with zipfile.ZipFile(f"{args.scraped_url_id}.zip", 'r') as zip_ref:
                zip_ref.extractall(f"{extractedPath}scrapedUrlId_{args.scraped_url_id.split('.')[0]}")
        else:
            print(f"File does not exists")
            return False

async def trigger_tests(url, primaryKeyword):
    global payload
    global domain_url

    async with async_playwright() as p:
        browser = await p.chromium.launch()  # headless = False
        context = await browser.new_context(user_agent = 'WEMASY CRAWLING')
            
        doesFileExist = await loadTraceFilesForSeoTest()
        if doesFileExist:
            # Start the context without tracing
            page = await context.new_page()

            html_file_name, html_content, trace_network = extract_html_file(f"{args.scraped_url_id}.zip")
            await page.goto(f'file://{base_path}/extracted/scrapedUrlId_{args.scraped_url_id}/resources/{html_file_name}')
            print("File exists")
        else:
            await context.tracing.start(name="trace", screenshots=True, snapshots=True)
            page = await context.new_page()
            try:
                await page.goto(url, timeout=60000)  
            except Exception as e:
                print(f"Error navigating to {url}: {e}")
                return
            await context.tracing.stop(path=f"{args.scraped_url_id}.zip")
            html_file_name, html_content, trace_network = extract_html_file(f"{args.scraped_url_id}.zip")
            print("File does not exist")
            
        # await googleListing.is_listed_on_google_business(url)
        
        paint_entries = await page.evaluate('''() => {return performance}''')        
        total_load_time = paint_entries['timing']['loadEventEnd'] - paint_entries['timing']['navigationStart']

        extract_words_from_body(f"{args.scraped_url_id}.zip")
        breadcrumb_res = breadcrumb.check_breadcrumbs(html_content)
        file_size = await check_file_size(f'{f"{args.scraped_url_id}.zip"}')

        is_file_size_satisfied = False
        print(f"File Size: {file_size.size}")

        # if seo_configurations["max_page_size"] == file_size.size:
            # is_file_size_satisfied = True

        await page.goto(f'file://{base_path}/extracted/scrapedUrlId_{args.scraped_url_id}/resources/{html_file_name}')
        content_number = await get_content_percentage(f'{base_path}/extracted/scrapedUrlId_{args.scraped_url_id}/resources/{html_file_name}')
        keyword_percentage = await get_primaryKeyword_percentage(f'{base_path}/extracted/scrapedUrlId_{args.scraped_url_id}/resources/{html_file_name}', primaryKeyword)

        
        html_number = len(html_content)
        print(f"Number: {html_number}")

        protocol, valid_till, new_protocol_version = extract_ssl_details(f"{args.scraped_url_id}.zip")

        network_array = extract_network_content(f"{args.scraped_url_id}.zip")
        network_payload = {
            'scraped_url_id': args.scraped_url_id,
            'network_array': network_array
        }
        # response = requests.post(f'{BASE_URL}/api/scrapers/network/create', json = network_payload, headers = headers)
        # print(response.json())
        
        content_payload = {
            'scraped_url_id': args.scraped_url_id,
            'breadcrumb': breadcrumb_res.is_satisfied,
            'file_size': file_size.size,
            'is_file_size_satisfied': is_file_size_satisfied,
            'page_speed': total_load_time,
            'content_percentage': round((content_number/html_number)*100, 4),
            'primary_key_percentage': keyword_percentage,
            'ssl_protocol': protocol,
            'valid_till': valid_till, 
            'new_protocol_version': new_protocol_version
        }
                                            
        # response = requests.post(f'{BASE_URL}/api/scrapers/urls/store_page_content', json = content_payload, headers = headers)
        # print(response.json())
        
        result = await robotTxt.check_robots_txt(url)
        if result.is_satisfied:
            await run_and_append_test(page, favicon.check_favicon, 'favicons', payload)
            await run_and_append_test(page, titleTag.check_title_tag, 'title_tags', payload)
            await run_and_append_test(page, metaDescription.check_meta_description, 'meta_descriptions', payload)
            await run_and_append_test(page, keywordOptimization.check_keyword_optimization, 'keyword_optimizations', payload)
            await run_and_append_test(page, imgTagsSizeDim.check_images, 'img_tags_size_dims', payload)
            await run_and_append_test(page, headerTag.check_header_tags, 'header_tags', payload)
            await run_and_append_test(page, metaTags.check_meta_data, 'meta_tags', payload)
            await run_and_append_test(page, sitemapSize.check_sitemap_size_and_links, 'sitemap_size_and_links', payload)
            await run_and_append_test(page, sitemapIndex.check_noindex_in_sitemap, 'sitemap_indexing', payload)
            await run_and_append_test(page, pageContent.check_content, 'check_page_content', payload)
            await run_and_append_test(page, httpLinks.check_http_links, 'http_links', payload)
            await run_and_append_test(page, doctype.check_doctype, 'doc_type', payload)
            await run_and_append_test(page, iframes.check_iframes, 'iframes_count', payload)
            await run_and_append_test(page, metaEncoding.check_meta_encoding, 'meta_encoding', payload)
            await run_and_append_test(page, resourcesCompression.check_compression, 'resources_compression', payload)
            await run_and_append_test(page, testOpenGraphProtocol.check_og_protocol, 'og_meta_content', payload)

            # await run_and_append_test(page, urlFormat.check_url_format, 'url_formats', payload)
            # await run_and_append_test(page, urlLength.check_url_length, 'url_length', payload)
            # await run_and_append_test(page, urlFormat.check_url_special_characters, 'url_length', payload)
            # await run_and_append_test(page, urlFormat.check_url_letters, 'url_length', payload)
            # await run_and_append_test(page, urlFormat.check_url_spelling, 'url_length', payload)
            # await run_and_append_test(page, contentEncoding.check_content_encoding, 'content_encoding', payload)
            # await run_and_append_test(page, canonicalURL.check_canonical_url, 'canonical_url', payload)
            # await run_and_append_test(page, assetsCaching.check_assets_caching, 'assets_caching', payload)
            
            print(f'\nPayload: {payload}\n')
            response = requests.post(f'{BASE_URL}/api/scrapers/urls/data/create', json=payload, headers=headers)
            print(response.json())
            if response.status_code == 201 or response.status_code == 200:
                print("API call successfull")
            else:
                print(f"API call failed with status code {response.status_code}")
        else:
            print('Crawler is not allowed on this page')

        await context.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

