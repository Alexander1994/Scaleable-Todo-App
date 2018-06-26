
import hashlib
from redis_client import redis_client
from flask import jsonify, request
from db import login as login_success
from bcrypt import gensalt



class User:
    def __verifyUser(self, username, sessionId):
        storedSessionId = redis_client.hmget(username, "sessionId")[0].decode('utf-8')
        return storedSessionId == sessionId

    def __genSessionId(self, username):
        salt = gensalt().decode('utf-8')
        return hashlib.sha256(bytearray(salt + username, 'utf8')).hexdigest()

    def login(self):
        error = None
        login_req = request.get_json()
        if "username" in login_req and "password" in login_req:
            username = login_req['username']
            password = login_req['password']
            
            if redis_client.exists(username): # if user already logged in return login attempt false
                return jsonify({'success':'false'})

            success = login_success(username, password)
            sessionId = None
            if success:
                sessionId = User.__genSessionId(self, username)
                default_session = {
                    'create a todo account':'complete',
                    'create todo':'incomplete',
                    'sessionId': sessionId,
                    'timeout': "TODO"
                }
                redis_client.hmset(username, default_session)

            return jsonify({'success':success, 'sessionId':sessionId})
        else:
            error = "please enter password"
        return jsonify({'error':error})

    def logout(self):
        error = None
        logout_req = request.get_json()
        sessionId = logout_req["sessionId"]
        username = logout_req['username']
        if "sessionId" in logout_req and User.__verifyUser(self, username, sessionId):
            redis_client.delete(username)
            return jsonify({'success': 'true'})
        return jsonify({'success':'false'})

    def signup(self):
        pass


user = User()

