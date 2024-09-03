from playwright.sync_api import sync_playwright
    
def mock_api_call(og_title, og_site_name):
    print(f"API Response: {og_title} - {og_site_name}")

def run_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        page.goto('https://85032.test.wemasy.nl/')
        page.click('a')
        
        og_title = page.evaluate('(document.querySelector(\'meta[property="og:title"]\') || {}).content')
        og_site_name = page.evaluate('(document.querySelector(\'meta[property="og:site_name"]\') || {}).content')
        
        # Mock API call
        mock_api_call(og_title, og_site_name)
        
        browser.close()

if __name__ == '__main__':
    run_playwright()