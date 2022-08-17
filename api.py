from flask import Flask, request, send_file
from flask_restful import Api, Resource, abort
from flask_cors import CORS
import bcrypt
from db import add_user, get_user, patch_user, add_like, get_users, get_matches, add_match, get_likes, get_room_msgs, user_login

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class Default(Resource):
    def get(self):
        return "Welcome to Pea Pod API! For a list of end points, try requesting to /api"

class Endpoints(Resource):
    def get(self):
        return send_file('./endpoints.json')

class GetUsers(Resource):
    def get(self):
        args = request.args
        interest = args.get('interest')
        try:
            return get_users(interest)
        except:
            return abort(400, message="Sorry, something went wrong...")

class User(Resource):
    def get(self, username):
        selected_user = get_user(username)
        if selected_user == 404: abort(404, message="Sorry, that user doesn't exist...")
        return selected_user

class UserLogin(Resource):
    def put(self, username):    
        body = request.get_json() 
        password = bcrypt.hashpw(body['password'], '')
        email = body['email']

        if password == None or email == None: return abort(400, message="Please supply a username and password")
        try:
            return add_user(username, password, email)
        except: 
            return abort(409, message="Sorry, that username is taken")

    def post(self, username):
        body = request.get_json()
        print(body['password'])
        password = bcrypt.hashpw(body['password'], '')

        return user_login(username, password)

class UpdateUser(Resource):
    def patch(self, username):
        body = request.get_json()
        args = ["bio", "gender", "avatar", "meme", "location", "interests"]
        print(body)
        try:
            for key in args:
                if key in body:
                    return patch_user(username, key, body[key]), 201
            
            return abort(400, message="Please attach a request body containing one of: gender, bio, avatar, meme, location, interests")
        except:
            return abort(400, message="Please attach a request body containing one of: gender, bio, avatar, meme, location, interests")

class IncomingLikes(Resource):
    def get(self, username):
        try:
            return get_likes(username)
        except:
            return abort(400, message="Sorry, something went wrong...")
    def patch(self, username):
        body = request.get_json()
        incoming_like = body['incoming_like']
        liked_detail = body['liked_detail']
        opening_message = body['opening_message']

        if incoming_like == None or liked_detail == None or opening_message == None: return abort(400, message="Please include an incoming like, liked detail, and opening message")
        try:
            return add_like(username, incoming_like, liked_detail, opening_message)
        except:
            return abort(400, message="Sorry, something went wrong...")

class HandleMatch(Resource):
    def get(self, username):
        return get_matches(username)

    def patch(self, username):
        body = request.get_json()
        new_match = body['new_match']

        if new_match == None: return abort(400, message="Please include the match's username")
        try:
            return add_match(username, new_match)
        except:
            return abort(400, message="Sorry, something went wrong... Is 'new_match' a real user?")

class Chat(Resource):
    def get(self, roomID):
        return get_room_msgs(roomID)


api.add_resource(Default, '/')
api.add_resource(Endpoints, '/api')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserLogin, '/user/<string:username>')
api.add_resource(UpdateUser, '/user/<string:username>/details')
api.add_resource(IncomingLikes, '/user/<string:username>/incoming_likes')
api.add_resource(GetUsers, '/users')
api.add_resource(HandleMatch, '/user/<string:username>/matches')
api.add_resource(Chat, '/chat/<string:roomID>/messages')

if __name__ == "__main__":
    app.run(debug=True)