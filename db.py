import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Pufferfish:Pufferfish@cluster0.pnqsntf.mongodb.net/?retryWrites=true&w=majority')

database = client.get_database('TestDB')
users_collection = database.get_collection('users')

def get_user(username):
    return users_collection.find_one({"_id": username})

def add_user(username, password):
    return users_collection.insert_one({"_id": username, username: {"password": password}})

def patch_user(username, key, value):
    if key == "interests":
        value = json.loads(value)
        print(value)
        users_collection.update_one({"_id": username}, {"$set": {username + "." + key: value}})
    else:
        users_collection.update_one({"_id": username}, {"$set": {username + "." + key: value}})