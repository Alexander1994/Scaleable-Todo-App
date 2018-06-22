
from flask import jsonify, request
from db import login as login_success

class User:
    def login(self):
        error = None
        login_req = request.get_json()
        if "username" in login_req and "password" in login_req:
            success = login_success(login_req['username'], login_req['password'])
            return jsonify({'success':success})
        else:
            error = "please enter password"
        return jsonify({'error':error})

    def logout(self):
        pass

    def signup(self):
        pass

user = User()

