async def check_content(page):
    
    class data(object): pass
    data.is_empty = True
    data.weight = 0
    data.content_len = 0   
    content = await page.content()
    data.content_len = len(content)
    if data.content_len > 0:
        data.is_empty = False
        data.weight = 1
            
    return data