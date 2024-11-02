import flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from dotenv import load_dotenv

import _db
import _user

load_dotenv()
app = flask.Flask(__name__)
api = Api(app)
CORS(app)

class User():
    class Login(Resource):
        def post(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                SELECT * FROM users
                WHERE user_username = '{data["username"]}'
                AND user_password = '{data["password"]}'
            """)
            response = cursor.fetchall()
            db.close()
            if len(response) == 0:
                return {"message": "Invalid credentials", "auth": False}, 401
            else:
                return {"message": "Login successful", "auth": True}, 200
        def delete(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                DELETE FROM users
                WHERE user_username = '{data["username"]}'
                AND user_password = '{data["password"]}'
            """)
            db.commit()
            db.close()
            return {"message": "User deleted successfully"}, 200
            
    class Register(Resource):
        def post(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                INSERT INTO users (user_username, user_password)
                VALUES ('{data["username"]}', '{data["password"]}')
            """)
            db.commit()
            db.close()
            return {"message": "User registered successfully"}, 200
    
    class Profile(Resource):
        def post(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                SELECT * FROM users
                WHERE user_username = '{data["username"]}'
                AND user_password = '{data["password"]}'
            """)
            response = cursor.fetchall()
            db.close()
            if len(response) == 0:
                return {"message": "Invalid credentials", "auth": False}, 401
            else:
                return {"message": "Profile fetched successfully", "auth": True}, 200
            
    class Update(Resource):
        def post(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                UPDATE users
                SET user_password = '{data["new_password"]}'
                WHERE user_username = '{data["username"]}'
                AND user_password = '{data["password"]}'
            """)
            db.commit()
            db.close()
            return {"message": "Password updated successfully"}, 200
        
    class Delete(Resource):
        def post(self):
            data = flask.request.json
            print("Request Data Recieved:", data)
            db = _db.Database()
            cursor = db.cursor()
            cursor.execute(f"""
                DELETE FROM users
                WHERE user_username = '{data["username"]}'
                AND user_password = '{data["password"]}'
            """)
            db.commit()
            db.close()
            return {"message": "User deleted successfully"}, 200

api.add_resource(User.Login, "/api/user/login")
api.add_resource(User.Register, "/api/user/register")
api.add_resource(User.Profile, "/api/user/profile")
api.add_resource(User.Update, "/api/user/update")
api.add_resource(User.Delete, "/api/user/delete")

if __name__ == "__main__":
    app.run(debug=True)