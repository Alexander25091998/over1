import requests
import json

response = requests.get('https://www.kufar.by/l/mebel')
mebel_data = response.text
data = mebel_data.split('title')
print(data)
# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204: