async def check_og_protocol(page):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    
    og_image = await page.query_selector('meta[property="og:image"]')
    og_type = await page.query_selector('meta[property="og:type"]')
    og_title = await page.query_selector('meta[property="og:title"]')
    og_description = await page.query_selector('meta[property="og:description"]')
    og_locale = await page.query_selector('meta[property="og:locale"]')
    
    if og_image and og_type and og_title and og_description and og_locale:
        data.is_satisfied = True
        data.weight = 1
        data.og_image = await og_image.get_attribute('content')
        data.og_type = await og_type.get_attribute('content')
        data.og_title = await og_title.get_attribute('content')
        data.og_description = await og_description.get_attribute('content')
        data.og_locale = await og_locale.get_attribute('content')
    else:
        data.og_image = ''
        data.og_type = ''
        data.og_title = ''
        data.og_description = ''
        data.og_locale = ''

    return data
