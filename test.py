import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'user/Bean')
print(response.json())
input()

response = requests.put(BASE + 'user/Moss', {
    "password": "Hello",
    "email": "anotherfakeemail@gmail.net"
})
print(response.json())
input()

response = requests.patch(BASE + 'user/Moss/details', {
    "bio": "Pretty much just the coolest guy ever"
})
print(response.json())

response = requests.patch(BASE + 'user/Moss/details', {
    "gender": "male"
})
print(response.json())

response = requests.patch(BASE + 'user/Moss/details', {
    "location": "Liverpool"
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
    "incoming_like": "Moss",
    "liked_detail": "bio",
    "opening_message": "I like beans"
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