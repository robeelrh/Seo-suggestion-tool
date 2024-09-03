async def check_url_length(url):
    
    class Data(object): pass
    
    data = Data()
    data.is_satisfied = False
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
                    data.is_satisfied = True
                    data.weight += 1
                    if tag != 'h1':
                        data.keyword_count_outside_h1 += 1
    return data
