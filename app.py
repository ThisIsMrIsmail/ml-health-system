import flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import os
from dotenv import load_dotenv
import db

load_dotenv()
app = flask.Flask(__name__)
api = Api(app)
CORS(app)

class Login(Resource):
    def post(self):
        data = flask.request.json
        print("Request Data Recieved:", data)
        cursor = db.cursor()
        cursor.execute(f"""
            SELECT * FROM users
            WHERE user_username = "{data["username"]}" AND user_password = "{data["password"]}"
        """)
        result = cursor.fetchall()
        print("Result:", result)
        if len(result) == 0:
            return {"data": "Invalid credentials"}
        else:
            return {"data": "Login successful"}
        # db.commit()

        

        # return {"data": "Registration data"}

api.add_resource(Login, "/api/login")

if __name__ == "__main__":
    app.run(debug=True)