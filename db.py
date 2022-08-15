import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Pufferfish:Pufferfish@cluster0.pnqsntf.mongodb.net/?retryWrites=true&w=majority')

database = client.get_database('TestDB')
users_collection = database.get_collection('users')

def get_user(username):
    user = users_collection.find_one({"_id": username})
    del user[username]["password"]
    return user

def add_user(username, password, email):
    users_collection.insert_one({"_id": username, username: {"password": password, "email": email, "incoming_likes": []}})
    return "User created!"

def patch_user(username, key, value):
    if key == "interests":
        value = json.loads(value)
        users_collection.update_one({"_id": username}, {"$set": {username + "." + key: value}})
    else:
        users_collection.update_one({"_id": username}, {"$set": {username + "." + key: value}})
    return "User update successful!"

def add_like(username, incoming_like):
    currentUser = users_collection.find_one({"_id": username})
    likes = currentUser[username]["incoming_likes"]
    if incoming_like not in likes:
        users_collection.update_one({"_id": username}, {"$push": {username + ".incoming_likes": incoming_like}})
        return incoming_like + " added to " + username + "'s incoming likes"
    else:
        return incoming_like + " has already liked " + username

def get_users(interest):
    arr = []
    for user in users_collection.find():
        del user[user["_id"]]["password"]
        if interest == None or interest in user[user["_id"]]["interests"]:
            arr.append(user)
    return arr