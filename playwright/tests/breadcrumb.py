import json

def check_breadcrumbs(html_content):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    
    if '<script type="application/ld+json">' in html_content:
            start_index = html_content.find('<script type="application/ld+json">')
            end_index = html_content.find('</script>', start_index)
            json_data = html_content[start_index + len('<script type="application/ld+json">'):end_index]

            res = json.loads(json_data)
            print(f'res: {res}')
            if "breadcrumb" in res:
                print("Breadcrumb structured data found in the HTML.")
                data.is_satisfied = True
                data.weight = 1

    return data
        
                