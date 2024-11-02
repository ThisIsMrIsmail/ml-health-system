import flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from db import db

app = flask.Flask(__name__)
api = Api(app)
CORS(app)

class Login(Resource):
    def post(self):
        print(flask.request.json)
        
        return {"data": "Registration data"}

api.add_resource(Login, "/api/login")

if __name__ == "__main__":
    app.run(debug=True)