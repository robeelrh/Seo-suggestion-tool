async def check_title_tag(page):
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    
    title_tag = await page.title()
    data.title = title_tag
    data.title_len = len(title_tag)
    
    if 50 <= data.title_len <= 70:
        data.is_satisfied = True
        data.weight = 1
    return data