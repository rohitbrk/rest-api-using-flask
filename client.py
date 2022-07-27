import json
import requests

BASE = "http://127.0.0.1:5000/"

data = {"name": "how to swim", "likes": 200, "views": 500}

response = requests.post(BASE+"video/6", json=data)
print(response.json())
input()
response = requests.get(BASE+"video/6")
print(response.json())
input()
data = {"name": "how to swim", "likes": 99, "views": 99}
response = requests.patch(BASE+"video/6", json=data)
print(response.json())
input()
response = requests.get(BASE+"video/6")
print(response.json())
input()
response = requests.delete(BASE+"video/6")
print(response.json())
input()
response = requests.get(BASE+"video/6")
print(response.json())
