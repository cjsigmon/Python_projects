import json
import requests


url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
json_dict = response.json()
print(json_dict)
print(json.dumps(json_dict, indent = 2,))