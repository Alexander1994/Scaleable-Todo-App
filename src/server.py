
from flask import Flask, jsonify, request
from db import login as login_success

class Server_Engine:
    def login(self):
        error = None
        login = request.get_json()
        print(type(login))
        if "username" in login and "password" in login:
            success = login_success(login['username'], login['password'])
            return jsonify({'success':success})
        else:
            error = "please enter password"
        return jsonify({'error':error})


server = Flask(__name__)
server_engine = Server_Engine()

