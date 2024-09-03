async def check_canonical_url(page):
    class Data(object): pass
    
    data = Data()
    data.is_satisfied = False
    data.weight = 0
    data.is_canonical = False
    data.url = ''
    
    canonical_url = await page.evaluate(
        """() => {
            const canonicalLink = document.querySelector("link[rel='canonical']");
            return canonicalLink ? canonicalLink.href : null;
        }"""
    )

    if canonical_url:
        data.is_canonical = True
        data.url = canonical_url
        
        if canonical_url.startswith("https://"):
            data.is_satisfied = True
            data.weight = 1
    else:
        print("No canonical URL found on the page")

    return data