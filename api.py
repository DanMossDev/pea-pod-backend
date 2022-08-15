from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from db import add_user, get_user, patch_user, add_like, get_users

app = Flask(__name__)
api = Api(app) 


user_signup_args = reqparse.RequestParser()
user_signup_args_arr = ["password", "email"]
for item in user_signup_args_arr:
    user_signup_args.add_argument(item, type=str, help="Please enter " + item, required=True, location='form')

user_login_args = reqparse.RequestParser()
user_login_args.add_argument("password", type=str, help="Please enter a password", required=True, location='form')

user_update_args = reqparse.RequestParser()
user_update_args_arr = ["gender", "bio", "avatar", "meme", "location", "interests"]
for item in user_update_args_arr:   
    user_update_args.add_argument(item, type=str, help="Please enter your" + item, required=False, location='form')

incoming_like_args = reqparse.RequestParser()
incoming_like_args.add_argument("incoming_like", type=str, help="Please include the username of the incoming like", required=True, location='form')

class Default(Resource):
    def get(self):
        return "Welcome to Pea Pod API! For a list of end points, try requesting to /api"

class User(Resource):
    def get(self, username):
        selected_user = get_user(username)
        if selected_user == 404: abort(404, message="Sorry, that user doesn't exist...")
        return selected_user

class UserLogin(Resource):
    def put(self, username):     
        args = user_signup_args.parse_args() #gets arguments off the body 
        password = args['password']
        email = args['email']
        try:
            return add_user(username, password, email)
        except: 
            return abort(409, message="Please enter one of the following: <string:bio>, <string:gender>, <string:location>, <string:interests>")

    def post(self, username):
        #return an auth token for the current user
        pass

class UpdateUser(Resource):
    def patch(self, username):
        args = user_update_args.parse_args()
        try:
            for key in args:
                if args[key] != None:
                    return patch_user(username, key, args[key]), 201
            return abort(400, message="Please attach a request body containing one of: gender, bio, avatar, meme, location, interests")
            
        except:
            return abort(400, message="Sorry, something went wrong...")

class IncomingLikes(Resource):
    def patch(self, username):
        args = incoming_like_args.parse_args()
        incoming_like = args['incoming_like']
        try:
            return add_like(username, incoming_like)
        except:
            return abort(400, message="Sorry, something went wrong...")

class GetUsers(Resource):
    def get(self):
        args = request.args
        interest = args.get('interest')
        try:
            return get_users(interest)
        except:
            return abort(400, message="Sorry, something went wrong...")

api.add_resource(Default, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserLogin, '/user/<string:username>')
api.add_resource(UpdateUser, '/user/<string:username>/details')
api.add_resource(IncomingLikes, '/user/<string:username>/incoming_likes')
api.add_resource(GetUsers, '/users')

if __name__ == "__main__":
    app.run(debug=True)