from flask import Flask
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
import uuid

app = Flask(__name__)
app.secret_key =  uuid.uuid4().hex
# creating a connection with mongodb
mongo = pymongo.MongoClient('mongodb://localhost:27017/')
users = mongo.users
users_details = users.users_details


@app.route('/users', methods=['GET','POST']) # GET to get all users and POST to add a user
def get_all_users_or_add():
    if request.method == 'GET':
        all_users = users.users_details.find()
        resp = dumps(all_users)
        return resp 

    elif request.method == 'POST':
        _json = request.json
        if ('name' in _json.keys()) and ('email' in _json.keys()) and ('password' in _json.keys()):
            _name = _json['name']
            _email = _json['email']
            _password = _json['password']
            _hashed_password = generate_password_hash(_password)
            users.users_details.insert_one({'name': _name, 'email': _email, 'password': _hashed_password})
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return {"Error": "Missing Data you need to pass name : <name> , email: <email>, password:<password> to add"}


@app.route('/users/<id>', methods=['GET','PUT','DELETE'])
def get_one_user(id):
    user = users.users_details.find_one({'_id': ObjectId(id)})
    if user is None:
        return {"Error": "User not found"}
    if request.method == 'GET':
        resp = dumps(user)
        return resp
    if request.method == 'PUT':
        _json = request.json
        if ('name' in _json.keys()) or ('email' in _json.keys()) or ('password' in _json.keys()): # check if any of the following is passed
            current_user = users.users_details.find_one({'_id': ObjectId(id)})
            print(current_user)
            _id = id
            _name = _json['name'] if 'name' in _json.keys() else current_user['name']# if name is passed then it is updated else it is the old name is used
            _email = _json['email'] if 'email' in _json.keys() else current_user['email']# if email is passed then it is updated else it is the old email is used
            _password = _json['password'] if 'password' in _json.keys() else None# if password is passed then it is updated else it is the old password is used
            _hashed_password = generate_password_hash(_password) if _password else current_user['password']# udpate password if password is passed else use the old password

            users.users_details.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, # if id is passed as string or object
            {'$set': {'name': _name
            , 'email': _email
            , 'password': _hashed_password}}) 
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return {"Error": "Missing you need to pass id and atleast one of the following name : <name> , email: <email>, password:<password> to update"}
    if request.method == 'DELETE':
        users_details.delete_one({'_id': ObjectId(id)})
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
if __name__ == "__main__":
    app.run(debug=True) 