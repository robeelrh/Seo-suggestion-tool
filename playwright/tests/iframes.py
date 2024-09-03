async def check_iframes(page):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    data.iframes_count = 0
    
    count = await page.evaluate('() => document.querySelectorAll("iframe").length')
    if count > 0:
        data.iframes_count = count
        data.is_satisfied = True
        data.weight = 1 
        
    return data