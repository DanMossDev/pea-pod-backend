import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'chat/Anakin%Padme/messages')
print(response.json())