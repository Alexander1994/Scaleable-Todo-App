
from app.views.user import user
from app.db import login as login_success
from app.redis_client import redis_client, get_todo_key, get_todo_dict
from flask import jsonify, request
import json


class Todo_Item:
    def add(self):
        error = None
        success = False
        req_json = user.validRequest(request)
        if req_json != None and 'add' in req_json:
            username = req_json['username']
            update_dict = req_json['add']
            if update_dict:
                todo_key = get_todo_key(username)
                redis_client.hmset(todo_key, update_dict)
                success = True
            else:
                error = "no update included"
            return jsonify({'success':success, 'error':error})
        else:
            error = "invalid login"
        return jsonify({'success':success, 'error':error})

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
            todo_json = get_todo_dict(req_json['username']) 
            return jsonify({'todo':todo_json, 'error':error})
        else:
            error = "invalid login"
        return jsonify({'todo':todo_json, 'error': error})



todo_item = Todo_Item()

