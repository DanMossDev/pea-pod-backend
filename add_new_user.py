import requests

BASE = "http://127.0.0.1:5000/"

username = input("Enter a username: ")

response = requests.put(BASE + 'user/' + username, data={
    "password": "Hello",
    "email": "afakeemail@gmail.net"
}, headers={'Content-Type': 'application/json; charset=utf-8'})
print(response.json())

response = requests.patch(BASE + 'user/' + username + '/details', {
    "bio": "Another test user, don't mind me!"
})
print(response.json())


response = requests.patch(BASE + 'user/' + username + '/details', {
    "gender": "male"
})
print(response.json())

response = requests.patch(BASE + 'user/' + username + '/details', {
    "meme": "https://www.youtube.com/watch?v=qN80_7rNmcE"
})
print(response.json())

response = requests.patch(BASE + 'user/' + username + '/details', {
    "location": "London"
})
print(response.json())

response = requests.patch(BASE + 'user/' + username + '/details', {
    "interests": '["gaming", "coding", "rugby", "reading", "music"]'
})
print(response.json())