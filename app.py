import flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from dotenv import load_dotenv
import _db


load_dotenv()
app = flask.Flask(__name__)
api = Api(app)
CORS(app)

class Login(Resource):
    def post(self):
        data = flask.request.json
        print("Request Data Recieved:", data)
        db = _db.Database()
        cursor = db.cursor()
        cursor.execute(f"""
            SELECT * FROM users
            WHERE user_username = '{data["username"]}' AND user_password = '{data["password"]}'
        """)
        response = cursor.fetchall()
        db.close()
        if len(response) == 0:
            return {"message": "Invalid credentials", "auth": False}, 401
        else:
            return {"message": "Login successful", "auth": True}, 200

api.add_resource(Login, "/api/login")

if __name__ == "__main__":
    app.run(debug=True)