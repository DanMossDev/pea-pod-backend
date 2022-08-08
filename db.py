from pymongo import MongoClient

client = MongoClient('mongodb+srv://Moss:<passwordhere>@peapod.3d4049y.mongodb.net/?retryWrites=true&w=majority')

database = client.get_database('main')
users_collection = database.get_collection('users')



def add_user(username, password):
    users_collection.insert_one({"username": username, "password": password})