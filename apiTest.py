from dotenv import load_dotenv
load_dotenv()
import os, requests, json
key = os.getenv('ASSURE_SUB_KEY')
service_address = os.getenv('SERVICE_ADDRESS')
img_service_portal = os.getenv('IMG_SERVICE_PORTAL')
full_addr = str(service_address)+str(img_service_portal)

print("address: "+full_addr)
# print("key: "+str(key))

img_path = './imgs/newYearsEve.jpg'
try:
    img_data = open(img_path,'rb').read()
    print(" File was accessed successfully.")

except FileNotFoundError:
    print("File couldn't be accessed!")

request_headers={
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': key
}
response = requests.post(full_addr, headers=request_headers, data=img_data)
response.raise_for_status()
result = response.json()
print("metadata of the image:"+str(result['metadata']))
