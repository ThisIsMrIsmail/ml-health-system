import flask
import json
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from dotenv import load_dotenv

import _db
import _user

load_dotenv()
app = flask.Flask(__name__)
api = Api(app)
CORS(app)

class DB(Resource):
    def post(self):
        conn = _db.Database()
        cursor = conn.cursor()
        result = cursor.execute(flask.request.json['query'])
        conn.commit()
        
        response_list = []
        for row in result.fetchall():
            print(type(row), row)
            tmp = []
            for i in row:
                tmp.append(i)
            response_list.append(tmp)

        return {"query_response", json.dumps(response_list)}, 200
    
class User(Resource):
    class Register(Resource):
        def post(self):
            return _user.Register(flask.request.json, _db.Database())
    class Login(Resource):
        def post(self):
            return _user.Login(flask.request.json, _db.Database())
    class Profile(Resource):
        def post(self):
            return _user.Profile(flask.request.json, _db.Database())
    class Update(Resource):
        def post(self):
            return _user.Update(flask.request.json, _db.Database())
    class Delete(Resource):
        def post(self):
            return _user.Delete(flask.request.json, _db.Database())

api.add_resource(User.Register, "/api/user/register")
api.add_resource(User.Login, "/api/user/login")
api.add_resource(User.Profile, "/api/user/profile")
api.add_resource(User.Update, "/api/user/update")
api.add_resource(User.Delete, "/api/user/delete")

api.add_resource(DB, "/api/db/query")

if __name__ == "__main__":
    app.run(debug=True)