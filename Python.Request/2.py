import requests
import json

response = requests.get("https://www.kufar.by/l/mebel")
data = json.loads(response.text)
data = data.split('</title>')
print()