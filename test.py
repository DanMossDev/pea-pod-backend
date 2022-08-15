import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'user/Bean')
print("get user")
print(response.json())
input()

response = requests.put(BASE + 'user/Moss', {
    "password": "Hello",
    "email": "anotherfakeemail@gmail.net"
})
print(response.json())
input()

response = requests.patch(BASE + 'user/Bean/details', {
    "bio": "Hi I am bean!!!"
})
print(response.json())

response = requests.patch(BASE + 'user/Bean/details', {
    "gender": "female"
})
print(response.json())

response = requests.patch(BASE + 'user/Bean/details', {
    "location": "Norfolk"
})
print(response.json())

response = requests.patch(BASE + 'user/Moss/details', {
    "interests": '["gaming", "coding", "rugby", "reading", "music"]'
})
print(response.json())
input()

response = requests.put(BASE + 'user/Morp', {
    "password": "Hello"
})
print(response.json())
input()

response = requests.patch(BASE + 'user/Bean/details')
print(response.json())
response = requests.patch(BASE + 'user/Bean/details', {
    "cheese": "Yes please, Gromit"
})
print(response.json())
input()

response = requests.patch(BASE + 'user/Bean/incoming_likes', {
    "incoming_like": "Moss"
})
print(response.json())
input()

response = requests.get(BASE + '/users?interest=gaming')
print(response.json())
input()

response = requests.get(BASE + '/users?interest=coding')
print(response.json())
input()

response = requests.get(BASE + '/users')
print(response.json())