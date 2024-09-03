import re
async def check_url_format(url):
    
    class data(object): pass
    data.is_satisfied = True
    data.url_length = 0
    data.weight = 1
    data.url_string = url
    data.url_length = len(url)
    
    if data.url_length > 500:
        data.is_satisfied = False
        data.weight = 0
        
    return data

async def check_url_special_characters(url):
    
    class data(object): pass
    data.is_satisfied = True
    data.weight = 1
    data.url = ''

    
    data.url = url
    if "_" in url:
        data.is_satisfied = False
        data.weight = 0
    
    return data

async def check_url_letters(url):
    
    class data(object): pass
    data.is_satisfied = True
    data.weight = 1
    data.url = ''

    data.url = url
    if any(c.isupper() for c in url):
        data.is_satisfied = False
        data.weight = 0
    
    return data

def check_url_spelling(url):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    data.url = ''

    data.url = url
    if url.endswith('/'):
        data.is_satisfied = True
        data.weight = 1
    
    return data