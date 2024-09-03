import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from title_tag.main import title_tag
import pandas as pd

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to fetch HTML content.")
        return None

def get_title_tag_length(soup):
    title_tag = soup.title
    if title_tag:
        return len(title_tag.text)
    else:
        return 0

def get_content_length(soup):
    content = soup.get_text()
    return len(content)

def is_favicon_present(soup):
    favicon = soup.find("link", rel="icon")
    return favicon is not None

def get_anchor_tag_protocols(soup):
    protocols = []
    anchor_tags = soup.find_all('a')
    for tag in anchor_tags:
        href = tag.get('href')
        if href:
            parsed_url = urlparse(href)
            protocols.append(parsed_url.scheme)
    return list(set(protocols))

def is_breadcrumb_structure(soup):
    breadcrumb_tag = soup.find_all(['ol', 'ul'])
    if breadcrumb_tag:
        for tag in breadcrumb_tag:
            items = tag.find_all('li')
            if len(items) > 1: 
                return True
    return False
def generate_title_tag_data(title_tag_length):
    is_satisfied = 0
    if 50<= title_tag_length <=70:
        is_satisfied = 1
    return pd.DataFrame({"title_length":[title_tag_length],"is_satisfied":is_satisfied})


def run_model(title_tag_length):
    print("Suggestions for title tag: ")
    title_tag(generate_title_tag_data(title_tag_length))

def main():
    url = input("Enter URL: ")
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag_length = get_title_tag_length(soup)
        content_length = get_content_length(soup)
        favicon_present = is_favicon_present(soup)
        anchor_tag_protocols = get_anchor_tag_protocols(soup)
        is_breadcrumb = is_breadcrumb_structure(soup)

        print(f"Title Tag Length: {title_tag_length}")
        print(f"Content Length: {content_length}")
        print(f"Favicon Present: {favicon_present}")
        print(f"Protocols of Anchor Tags: {anchor_tag_protocols}")
        print(f"Breadcrumb Structure Present: {is_breadcrumb}")
    else:
        print("Exiting...")

    print()
    run_model(title_tag_length)

if __name__ == "__main__":
    main()
