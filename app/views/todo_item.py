
from app.db import login as login_success
from app.redis_client import redis_client
from app.views.user import user
from flask import jsonify, request
import json


class Todo_Item:
    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


    def list_all(self):
        error = None
        todo_json = None
        json_req = request.get_json()
        req_json = user.validRequest(request)
        if req_json != None:
            username = req_json['username']
            data = redis_client.hmget(username, 'todo')
            todo_json = json.loads(data[0].decode('utf-8')) # To reduce load on the server, the json could be loaded client side
            return jsonify({'todo':todo_json, 'error':error})
        else:
            error = "invalid login"
        return jsonify({'todo':todo_json, 'error': error})



todo_item = Todo_Item()

