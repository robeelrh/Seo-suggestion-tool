async def check_meta_encoding(page):
    
    class data(object): pass
    data.is_satisfied = False
    data.meta_encoding = False
    data.weight = 0

    meta_tag = await page.query_selector('meta[charset="utf-8"]')
    print(meta_tag)
    if meta_tag:
        data.meta_encoding = True
        data.is_satisfied = True
        data.weight = 1
    
    return data
        