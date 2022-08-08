import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'user/Moss')
print("get Moss")
print(response.json())
input()

response = requests.put(BASE + 'user/Bean', {
    "password": "Hello"
})
print(response.json())
input()