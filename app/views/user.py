
import hashlib
from app.redis_client import redis_client
from flask import jsonify, request
from app.db import login as login_success
from bcrypt import gensalt


class User:
    def __userIsLoggedIn(self, username):
        return bool(redis_client.exists(username))

    def __logoutUser(self, username):
        redis_client.delete(username)

    def __verifyUser(self, username, sessionId):
        storedSessionId = redis_client.hmget(username, "sessionId")[0].decode('utf-8')
        return storedSessionId == sessionId

    def __genSessionId(self, username):
        salt = gensalt().decode('utf-8')
        return hashlib.sha256(bytearray(salt + username, 'utf8')).hexdigest()


    def login(self):
        error = None
        sessionId = None
        login_req = request.get_json()
        if "username" in login_req and "password" in login_req:
            username = login_req['username']
            password = login_req['password']
            
            if not User.__userIsLoggedIn(self, username):
                success = login_success(username, password)
                if success:
                    sessionId = User.__genSessionId(self, username)
                    default_session = {
                        'create a todo account':'complete',
                        'create todo':'incomplete',
                        'sessionId': sessionId,
                        'timeout': "TODO"
                    }
                    redis_client.hmset(username, default_session)
                else:
                    error = "username or password is incorrect"
                return jsonify({'success':success, 'sessionId':sessionId, 'error':error})
            else:
                 error = "User currently logged in" # if user already logged in return login attempt false
        else:
            error = "username or password not included in request"
        return jsonify({'success':False, 'sessionId':sessionId, 'error':error})

    def logout(self):
        error = None
        logout_req = request.get_json()
        if "sessionId" in logout_req and "username" in logout_req:
            sessionId = logout_req["sessionId"]
            username = logout_req['username']
            if User.__verifyUser(self, username, sessionId):
                User.__logoutUser(self, username)   
                return jsonify({'success': 'true', 'error':error})
            else:
                error = "invalid logout" # sessionId doesn't match server id??? Bug or hacking maybe?
        else:
            error = "sessionId or username not included in logout"
        return jsonify({'success':'false', 'error':error})

    def signup(self):
        pass


user = User()

