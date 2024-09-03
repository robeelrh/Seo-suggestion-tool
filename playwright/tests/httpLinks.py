async def check_http_links(page):
    
    class data(object): pass
    data.is_satisfied = True
    data.http_satisfied = True
    data.https_satisfied = True
    data.http_links = []
    data.weight = 0
    
    links = await page.query_selector_all('a')
        
    for link in links:
        href = await link.get_attribute('href')
        
        if href and href.startswith('http://'):
            data.https_satisfied = False
            data.is_satisfied = False
            data.http_links.append(href)

    if data.is_satisfied:
        data.weight = 1
            
    return data