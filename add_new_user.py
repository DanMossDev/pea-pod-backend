import requests

BASE = "https://pea-pod-api.herokuapp.com/"

username = input("Enter a username: ")

response = requests.put(BASE + 'user/' + username, {
    "password": "Hello",
    "email": "afakeemail@gmail.net"
})
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