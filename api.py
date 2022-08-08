from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app) 


user_signup_args = reqparse.RequestParser()
user_signup_args.add_argument("password", type=str, help="Please enter a password", required=True, location='form')

user_login_args = reqparse.RequestParser()
user_login_args.add_argument("password", type=str, help="Please enter a password", required=True, location='form')

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("gender", type=str, help="Please enter your gender", required=False, location='form')
user_update_args.add_argument("bio", type=str, help="Please enter your bio", required=False, location='form')
user_update_args.add_argument("avatar", type=str, help="Please enter your avatar", required=False, location='form')
user_update_args.add_argument("meme", type=str, help="Please enter your meme", required=False, location='form')
user_update_args.add_argument("location", type=str, help="Please enter your location", required=False, location='form')
user_update_args.add_argument("interests", type=str, help="Please enter your interests", required=False, location='form')


# Test Dictionary
users = {
    "Moss": {
        "gender": "male",
        "bio": "Coolest guy ever",
        "avatar": "somehow store an image",
        "meme": "https://www.youtube.com/shorts/qN80_7rNmcE",
        "location": "Liverpool",
        "interests": ["gaming", "reading", "coding", "theatre", "music"],
        "password": "verysecret123"
    },
    "Sally": {
        "gender": "female",
        "bio": "Coolest gal ever",
        "avatar": "somehow store an image",
        "meme": "https://www.youtube.com/shorts/Jbnel9wB7Ik",
        "location": "Newcastle",
        "interests": ["gaming", "reading", "coding", "theatre", "music"],
        "password": "alsoverysecret123"
    }
}


class User(Resource):
    def get(self, username):
        #access the DB and get the user
        #return the
        return users[username]

class UserLogin(Resource):
    def put(self, username):
        #somehow get the users object from DB
        if username  in users: abort(409, message="Sorry, that username is already taken...")
        
        args = user_signup_args.parse_args() #gets arguments off the body 
        return args

    def get(self, username):
        #return an auth token for the current user
        pass

class UpdateUser(Resource):
    def patch(self, user_id):
        args = user_update_args.parse_args()
        print(args)


api.add_resource(User, '/user/<string:username>')
api.add_resource(UserLogin, '/user/<string:username>')
api.add_resource(UpdateUser, '/user/<string:username>/details')

if __name__ == "__main__":
    app.run(debug=True)