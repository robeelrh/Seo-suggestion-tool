async def check_meta_description(page):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    data.description = ''
    data.description_length = 0
    
    meta_description = await page.query_selector('meta[name="description"]')
    if meta_description:
        data.description = await meta_description.get_attribute('content')
        
    data.description_length = len(data.description)
    if 155 <= data.description_length <= 300:
        data.is_satisfied = True
        data.weight = 1
    
    return data