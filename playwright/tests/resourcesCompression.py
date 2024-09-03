async def check_compression(page):
    
    class data(object): pass
    data.content = []
    
    requests = await page.evaluate("window.performance.getEntriesByType('resource')")

    # Check each request for compression
    for request in requests:
        if request['initiatorType'] in ['script', 'link']:
            data.content.append({ 'url': request['name'], 'content_encoding': request.get('response', {}).get('contentEncoding', 'Not Compressed') })
            
    return data