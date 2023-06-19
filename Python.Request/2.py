import requests
import json
from bs4 import BeautifulSoup


response = requests.get('https://www.kufar.by/l/mebel')
mebel_data = response.text
data = mebel_data.split('title')
print()
# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204: