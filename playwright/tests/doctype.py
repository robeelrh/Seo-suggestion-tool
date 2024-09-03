async def check_doctype(page):
    
    class data(object): pass
    data.is_satisfied = False
    data.doctype = False
    data.weight = 0
    
    content = await page.content()
    
    if content[0:9].lower() == '<!doctype':
        
        data.is_satisfied = True
        data.doctype = True
        data.weight += 1 
        
    return data