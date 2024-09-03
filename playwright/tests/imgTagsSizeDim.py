import requests
async def check_images(page):
    
    class data(object): pass
    data.is_alt_satisfied = True
    data.is_size_satisfied = True
    data.is_dimension_satisfied = True
    data.is_satisfied = False
    data.weight = 0
    
    data.missing_alt_tags = []
    data.with_alt_tags = []
    
    data.correct_size = []
    data.large_size = []
    
    data.correct_dimensions = []
    data.incorrect_dimensions = []
    
    for image in await page.query_selector_all('img'):
        
        alt_tag = await image.get_attribute('alt')
        image_url = await image.get_attribute('src')

        if image_url is not None:
            
            if alt_tag:
                data.with_alt_tags.append({'image_url': image_url, 'alt_tag': alt_tag})
            else:
                data.is_alt_satisfied = False
                data.missing_alt_tags.append({'image_url': image_url, 'alt_tag': ''})

            width = await image.get_attribute('width')
            height = await image.get_attribute('height')

            if width and height:
                data.correct_dimensions.append({'image_url': image_url, 'width': width, 'height': height})
            else:
                data.is_dimension_satisfied = False
                data.incorrect_dimensions.append({'image_url': image_url, 'width': width, 'height': height})

            try:
                response = requests.head(image_url)
                size_kb = int(response.headers.get('content-length', 0)) / 1024

                if size_kb < 1000:
                    data.correct_size.append({'image_url': image_url, 'size_kb': size_kb})
                else:
                    data.is_size_satisfied = False
                    data.large_size.append({'image_url': image_url, 'size_kb': size_kb})
            except requests.RequestException as e:
                print(f"Error checking image attributes for {image_url}: {e}")


    conditions = [data.is_alt_satisfied, data.is_size_satisfied, data.is_dimension_satisfied]
    data.weight += sum(1 for condition in conditions if condition)
    if data.is_alt_satisfied and data.is_size_satisfied and data.is_dimension_satisfied:
        data.is_satisfied = True
        
    return data