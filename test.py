import requests

BASE = "http://127.0.0.1:5000/"

input("This is the standard GET user")
response = requests.get(BASE + 'user/Bean')
print(response.json())

input("This is a PUT for a user that already exists")
response = requests.put(BASE + 'user/Moss', {
    "password": "Hello",
    "email": "anotherfakeemail@gmail.net"
})
print(response.json())

input("This is a PUT for a user with insufficient data")
response = requests.put(BASE + 'user/Morp', {
    "password": "Hello"
})
print(response.json())

input("Bad details updates")
response = requests.patch(BASE + 'user/Bean/details')
print(response.json())
response = requests.patch(BASE + 'user/Bean/details', {
    "cheese": "Yes please, Gromit"
})
print(response.json())

input("users with gaming query")
response = requests.get(BASE + '/users?interest=gaming')
print(response.json())

input("Users with coding query")
response = requests.get(BASE + '/users?interest=coding')
print(response.json())

input("Users with no query")
response = requests.get(BASE + '/users')
print(response.json())
input()

user = input("Pick a user whose likes you want to see: ")
response = requests.get(BASE + '/user/' + user + '/incoming_likes')
print(response.json())

username = input("The user you want to like: ")
incoming_like = input("Your username: ")
response = requests.patch(BASE + 'user/' + username + '/incoming_likes', {
    "incoming_like": incoming_like,
    "liked_detail": "interests[4]",
    "opening_message": "Nice shoes"
})
print(response.json())