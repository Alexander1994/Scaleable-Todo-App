
import hashlib, json
from app.redis_client import redis_client
from flask import jsonify, request
from app.db import login as login_success
from app.redis_client import get_todo_key
from bcrypt import gensalt


class User:
    def __userIsLoggedIn(self, username):
        return bool(redis_client.exists(username))

    def __logoutUser(self, username):
        redis_client.delete(username)

    def __genSessionId(self, username):
        salt = gensalt().decode('utf-8')
        return hashlib.sha256(bytearray(salt + username, 'utf8')).hexdigest()

    def verifyUser(self, username, sessionId):
        sessionIdList = redis_client.hmget(username, "sessionId")
        if sessionIdList[0] == None:
            return False
        storedSessionId = sessionIdList[0].decode('utf-8')
        return storedSessionId == sessionId

    def validRequest(self, request):
        json_req = request.get_json()
        if "sessionId" in json_req and "username" in json_req:
            if self.verifyUser(json_req['username'], json_req["sessionId"]):
                return json_req
        return None

    def login(self):
        error = None
        sessionId = None
        login_req = request.get_json()
        if "password" in login_req and "username" in login_req:
            username = login_req['username']
            password = login_req['password']
            if not self.__userIsLoggedIn(username):
                success = login_success(username, password)
                if success:
                    sessionId = self.__genSessionId(username)
                    default_session = {
                        'sessionId': sessionId,
                        'timeout': "TODO"
                    }
                    todo_json = {
                        "create a todo account":"complete",
                        "create todo":"incomplete"
                    }
                    redis_client.hmset(username, default_session)
                    todo_key = get_todo_key(username)
                    redis_client.hmset(todo_key, todo_json)
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
        req_json = self.validRequest(request)
        if req_json != None:
            username = req_json['username']
            self.__logoutUser(username)   
            return jsonify({'success': 'true', 'error':error})
        else:
            error = "sessionId or username not included in logout"
        return jsonify({'success':'false', 'error':error})

    def signup(self):
        pass


user = User()

