import argparse, requests, asyncio, re, bs4, os, json
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('--scraped_url_id', type=str)

args = parser.parse_args()
image_url = ''

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
}

async def main():
    global image_url
    data = await getImageTestData(args.scraped_url_id)

    for dataArray in json.loads(data["missing_alt_tags"]) + json.loads(data["with_alt_tags"]) + json.loads(data["correct_size"]) + json.loads(data["large_size"]) + json.loads(data["correct_dimensions"]) + json.loads(data["incorrect_dimensions"]):

        imageResponse = await checkImages(dataArray["image_url"])
        if imageResponse.status_code == 200:
            print(f"Image Exists: {imageResponse.status_code}")
        else:
            print(f"Image not found: {imageResponse.status_code}")

async def getImageTestData(id):
    response = requests.post(f'{BASE_URL}/api/seo/get_images_data', json={"scraped_url_id": id}, headers=headers)
    data = response.json()
    return data[0]

async def checkImages(image_link):
    response = requests.head(image_link, headers = headers)
    return response

if __name__ == '__main__':
    asyncio.run(main())
