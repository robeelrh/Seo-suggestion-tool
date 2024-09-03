async def check_favicon(page):
    
    class data(object): pass

    data.is_satisfied = False
    data.weight = 0
    
    faviconSelector = await page.query_selector('link[rel="icon"]') or await page.query_selector('link[rel="shortcut icon"]')
    faviconLink = await faviconSelector.get_attribute('href')        
        
    if faviconLink:
        data.link = faviconLink
        data.favicon = True
        data.is_satisfied = True
        data.weight = 1

    return data