import json
from pymongo import MongoClient
import os
from defaultavatar import default_avatar

client = MongoClient(os.environ.get('DBURL'))

database = client.get_database('TestDB')
users_collection = database.get_collection('users')
chatdb = client.get_database('ChatDB')
messages_collection = chatdb.get_collection('messages')

def get_user(username):
    user = users_collection.find_one({"_id": username})
    if user == None: return 404
    del user[username]["password"]
    return user

def add_user(username, password, email):
    users_collection.insert_one({"_id": username, username: {"password": password, "email": email, "incoming_likes": [], "matches": [], "avatar": default_avatar}})
    return "User created!"

def user_login(username, password):
    user = users_collection.find_one({"_id": username})
    print(user[username]["password"])
    print(password)
    if user[username]["password"] == password: return "Login successful!", 200
    else: return "Incorrect password...", 403

def patch_user(username, key, value):
    users_collection.update_one({"_id": username}, {"$set": {username + "." + key: value}})
    return "User update successful!"

def get_likes(username):
    currentUser = users_collection.find_one({"_id": username})
    return currentUser[username]["incoming_likes"]

def add_like(username, incoming_like, liked_detail, opening_message):
    currentUser = users_collection.find_one({"_id": username})
    likes = currentUser[username]["incoming_likes"]
    like_avatar = users_collection.find_one({"_id": incoming_like})[incoming_like]["avatar"]

    for like in likes:
        if like["name"] == incoming_like: return incoming_like + " has already liked " + username

    users_collection.update_one({"_id": username}, {"$push": {username + ".incoming_likes": {"name": incoming_like, "liked_detail": liked_detail, "opening_message": opening_message, "avatar": like_avatar}}})
    return incoming_like + " added to " + username + "'s incoming likes"

def get_users(interest):
    arr = []
    for user in users_collection.find():
        del user[user["_id"]]["password"]
        if interest == None or interest in user[user["_id"]]["interests"]:
            arr.append(user)
    return arr

def get_matches(username):
    user = users_collection.find_one({"_id": username})
    return user[username]["matches"]

def add_match(username, new_match):
    user = users_collection.find_one({"_id": username})
    match_avatar = users_collection.find_one({"_id": new_match})[new_match]["avatar"]
    
    for match in user[username]["matches"]:
        if match["name"] == new_match: return "Sorry, that user is already a match", 400

    print('getting here')

    users_collection.update_one({"_id": username}, {"$pull": {username + ".incoming_likes": {"name": new_match}}})
    users_collection.update_one({"_id": username}, {"$push": {username + ".matches": {"name": new_match, "avatar": match_avatar}}})
    return new_match + " added to " + username + "'s matches", 201


def get_room_msgs(roomID):
    arr = []
    for msg in messages_collection.find({"room_id": roomID}):
        msg["_id"] = str(msg["_id"])
        arr.append(msg)
    return sorted(arr, key=lambda x: x['created_at'])