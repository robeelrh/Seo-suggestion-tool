from dotenv import load_dotenv
import requests, os

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

async def check_meta_data(page, seo_configurations):
    
    class data(object): pass
    data.is_satisfied = False
    data.is_description_length_satisfied = False
    data.is_title_length_satisfied = False
    data.weight = 0
    
    # Mandatory
    properties = ['og:title', 'og:type', 'og:url', 'og:image', 'og:description', 'og:site_name']
    meta_data = {}
    for prop in properties:
        selector = f'meta[property="{prop}"]'
        element = await page.query_selector(selector)
        if element:
            meta_data[prop] = await element.get_attribute('content')
    
    og_title_content = meta_data.get('og:title', None)
    og_type_content = meta_data.get('og:type', None)
    og_url_content = meta_data.get('og:url', None)
    og_image_content = meta_data.get('og:image', None)
    og_description_content = meta_data.get('og:description', None)
    og_site_name_content = meta_data.get('og:site_name', None)

    

    if og_description_content and seo_configurations["meta_tag_description_min_length"] < len(og_description_content) > seo_configurations["meta_tag_description_max_length"]:
        data.is_description_length_satisfied = True

    if og_title_content and seo_configurations["meta_tag_title_min_length"] < len(og_title_content) > seo_configurations["meta_tag_title_max_length"]:
        data.is_title_length_satisfied = True
    
    if all([og_title_content, og_type_content, og_url_content, og_image_content, og_description_content, og_site_name_content]):
        data.is_satisfied = True
        data.weight = 1
   
    # Optional
    twitter_properties = ['twitter:card', 'twitter:description', 'twitter:title', 'twitter:site', 'twitter:image', 'twitter:creator']
    twitter_meta_data = {}
    for twitter_prop in twitter_properties:
        twitter_selector = f'meta[name="{twitter_prop}"]'
        twitter_element = await page.query_selector(twitter_selector)
        if twitter_element:
            twitter_meta_data[twitter_prop] = await twitter_element.get_attribute('content')
    
    twitter_card = twitter_meta_data.get('twitter:card', None)
    twitter_description = twitter_meta_data.get('twitter:description', None)
    twitter_title = twitter_meta_data.get('twitter:title', None)
    twitter_site = twitter_meta_data.get('twitter:site', None)
    twitter_image = twitter_meta_data.get('twitter:image', None)
    twitter_creator = twitter_meta_data.get('twitter:creator', None)
    
    if all([twitter_card, twitter_description, twitter_title, twitter_site, twitter_image, twitter_creator]):
        data.weight = 2
            
    return data
