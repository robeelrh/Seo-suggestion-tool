from dotenv import load_dotenv
import requests, os

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

async def check_header_tags(page, primary_keyword, seo_configurations):
    
    class Data(object): pass
    
    data = Data()
    data.is_satisfied = False
    data.is_h2_satisfied = False
    data.weight = 0
    data.headers = []
    data.keyword_count_outside_h1 = 0
    
    header_tags = [f'h{i}' for i in range(1, 7)]
    
    for tag in header_tags:
        headers_text = await page.query_selector_all(tag)
        if headers_text:
            for header_text in headers_text:
                header_content = await header_text.inner_text()
                data.headers.append(header_content)
                if primary_keyword.lower() in header_content.lower():
                    
                    data.weight += 1
                    if tag != 'h1':
                        data.keyword_count_outside_h1 += 1
                    elif tag == 'h1' and len(header_content) <= seo_configurations["max_h1_header_length"]:
                        data.is_satisfied = True
                    elif tag == 'h2' and len(header_content) <= seo_configurations["max_h2_header_length"]:
                        data.is_h2_satisfied = True
    return data