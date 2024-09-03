async def check_keyword_optimization(page, primary_keyword):
    
    class data(object): pass
    data.is_primary_satisfied = False
    data.is_secondary_atisfied = True
    data.primary_keyword = ''
    data.primary_count = 0
    data.weight = 0
    
    content = await page.content()
    
    data.primary_count = content.lower().count(primary_keyword.lower())

    if data.primary_count > 0:
        data.is_primary_satisfied = True
        data.weight = 1     
        
    return data