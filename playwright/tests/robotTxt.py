import requests
from playwright.async_api import async_playwright
from requests.exceptions import Timeout

async def check_robots_txt(url):
    
    class data(object): pass
    data.is_satisfied = False
    data.weight = 0
    
    robots_url = url.rstrip('/') + '/robots.txt'

    try:
        response = requests.get(robots_url, timeout=10)
        if response.status_code == 200:
            content = response.text

            for line in content.splitlines():
                if line.lower().startswith("user-agent: *"):
                    
                    # Check for Disallow directives
                    if "disallow:" in line.lower():
                        
                        if url.lstrip("/").startswith(line.split(":", 1)[1].strip()):
                            data.is_satisfied = False
                            data.weight = 0
                            break
                        
                    # Check for Allow directives
                    elif "allow:" in line.lower():
                        # Check for specific path allow
                        if url.lstrip("/").startswith(line.split(":", 1)[1].strip()):
                            data.is_satisfied = True
                            data.weight = 1
                            break

            if data.weight == 0:
                async with async_playwright() as p:
                    browser = await p.chromium.launch()
                    page = await browser.new_page()
                    await page.goto(url)
            
                    await page.goto(url)
                    # html_content = await page.content()
                    meta_tag = await page.query_selector('meta[name="robots"]')
                    if meta_tag:
                        meta_content = await meta_tag.get_attribute('content')
                        if meta_content and meta_content.lower() == 'noindex':
                            data.is_satisfied = False
                            data.weight = 0
                        else:
                            data.is_satisfied = True
                            data.weight = 1
                    else:
                        print("No 'robots' meta tag found.")
                        data.is_satisfied = True
                        data.weight = 1
        else:
            print(f"Failed to fetch robots.txt. Status code: {response.status_code}")
    except Timeout:
        print("Request for robots.txt timed out.")
        data.is_satisfied = False
        data.weight = 0
    except requests.RequestException as e:
        print(f"Error fetching robots.txt: {e}")
        data.is_satisfied = False
        data.weight = 0
        
    return data     
