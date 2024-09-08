import zipfile, json, os, requests, re
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

def is_image(file_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    file_extension = get_file_extension(file_path)
    return file_extension in image_extensions

def upload_image_to_db(image_path, scraped_url_id):
    with open(image_path, 'rb') as file:
        files = {'image': (os.path.basename(image_path), file), 'scraped_url_id': scraped_url_id}
        response = requests.post(f'{BASE_URL}/api/scrapers/upload/image', files=files)
        return response

def extract_html_file(zip_path):
    extractedPath = f"{os.getcwd()}/extracted/"
    print(f"THIS IS PATH", extractedPath)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}")
        
    for root, dirs, files in os.walk(extractedPath):
        for file in files:
            output = is_image(file)
            # if output == True:
            #     response = upload_image_to_db(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/resources/{file}", zip_path.split('.')[0])
            #     print(f"Uploaded image {file} with status code: {response.status_code}")
        
    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/trace.network", "r") as f:
        trace_network = f.read()
                
        json_objects = [json.loads(obj) for obj in trace_network.split('\n') if obj.strip()]
        
        # print("json_object: ", json_objects[1]["snapshot"]["response"]["content"]["_sha1"])
        html_file = json_objects[0]["snapshot"]["response"]["content"]["_sha1"]
        # html_file = json_objects[0]["snapshot"]["response"]["content"]["_sha1"]
        print("html_file: ", html_file)
    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/resources/{html_file}", 'r', encoding='utf-8') as file:
        content = file.read()
        return html_file, content, trace_network
    
def extract_network_content(zip_path):
    request_payload = []
    extractedPath = f"{os.getcwd()}/extracted/"
        
    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/trace.network", "r") as f:
        trace_network = f.read()
        json_objects = [json.loads(obj) for obj in trace_network.split('\n') if obj.strip()]
        for item in json_objects:
            
            request_details = item["snapshot"]["request"]["url"]
            request_time = item["snapshot"]["time"]
            request_status = item["snapshot"]["response"]["status"]
            
            request_payload.append({"url": request_details, 'status_code': request_status, 'time': request_time })
            
        return request_payload
    
def extract_ssl_details(zip_path):
    extractedPath = f"{os.getcwd()}/extracted/"
        
    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/trace.network", "r") as f:
        trace_network = f.read()
                
        json_objects = [json.loads(obj) for obj in trace_network.split('\n') if obj.strip()]
        protocol = json_objects[0]["snapshot"]["_securityDetails"]["protocol"]
        valid_till = json_objects[0]["snapshot"]["_securityDetails"]["validTo"]
                
        if protocol[4:7] == '1.0':
            new_protocol_version = False
            print('Old Certificate')
        else: 
            new_protocol_version = True
            print('New Certificate')
        
    return protocol, valid_till, new_protocol_version

def extract_words_from_body(zip_path):
    extractedPath = f"{os.getcwd()}/extracted/"

    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/trace.network", "r") as f:
        trace_network = f.read()
                
        json_objects = [json.loads(obj) for obj in trace_network.split('\n') if obj.strip()]
        html_file = json_objects[0]["snapshot"]["response"]["content"]["_sha1"]

    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/resources/{html_file}", 'r', encoding='utf-8') as file:
        content = file.read()

        content = re.sub(r'<.*?>', '', content)
        content = re.sub(r'<head>.*?</head>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'style=".*?"', '', content)
        
        words = re.findall(r'\b\w+\b', content)
        words = [word for word in words if not word.startswith('http') and not word.startswith('www') and not word.isdigit()]
        # print(f'Extracted words: {words}')
        return words
        # return words

async def check_file_size(zip_path):
    extractedPath = f"{os.getcwd()}/extracted/"

    with open(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/trace.network", "r") as f:
        trace_network = f.read()
                
        json_objects = [json.loads(obj) for obj in trace_network.split('\n') if obj.strip()]
        html_file = json_objects[0]["snapshot"]["response"]["content"]["_sha1"]
    
    class data(object): pass
    data.size = 0
    
    data.size = round(os.path.getsize(f"{extractedPath}scrapedUrlId_{zip_path.split('.')[0]}/resources/{html_file}") / 1024 / 1024, 2)
    
    return data