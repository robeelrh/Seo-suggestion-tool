from playwright.async_api import async_playwright
import asyncio, argparse, time

async def save_pdf_file():
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
            
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto(args.url)
        time.sleep(5)
        await page.pdf(path=f"./files/{(args.url).replace('/', '_')}.pdf", format="A4", width='1920', height='1080')
        
        await page.close()
        await browser.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    
    asyncio.run(save_pdf_file())

