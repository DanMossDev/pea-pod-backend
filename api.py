from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db import add_user, get_user, patch_user

app = Flask(__name__)
api = Api(app) 


user_signup_args = reqparse.RequestParser()
user_signup_args.add_argument("password", type=str, help="Please enter a password", required=True, location='form')

user_login_args = reqparse.RequestParser()
user_login_args.add_argument("password", type=str, help="Please enter a password", required=True, location='form')

user_update_args = reqparse.RequestParser()
user_update_args_arr = ["gender", "bio", "avatar", "meme", "location", "interests"]
for item in user_update_args_arr:   
    user_update_args.add_argument(item, type=str, help="Please enter your" + item, required=False, location='form')



class User(Resource):
    def get(self, username):
        return get_user(username)

class UserLogin(Resource):
    def put(self, username):     
        args = user_signup_args.parse_args() #gets arguments off the body 
        password = args['password']
        try:
            add_user(username, password)
            return "User created!"
        except: 
            return abort(409, message="Sorry, that username is already taken...")

    def post(self, username):
        #return an auth token for the current user
        pass

class UpdateUser(Resource):
    def patch(self, username):
        args = user_update_args.parse_args()
        print(args)
        try:
            for key in args:
                if args[key] != None:
                    return patch_user(username, key, args[key]), 201
            
        except:
            return abort(400, message="Sorry, something went wrong...")


api.add_resource(User, '/user/<string:username>')
api.add_resource(UserLogin, '/user/<string:username>')
api.add_resource(UpdateUser, '/user/<string:username>/details')

if __name__ == "__main__":
    app.run(debug=True)