
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
            if update_dict and isinstance(update_dict, dict):
                todo_key = get_todo_key(username)
                redis_client.hmset(todo_key, update_dict)
                success = True
            else:
                error = "no addition included"
        else:
            error = "invalid login"
        return jsonify({'success':success, 'error':error})

    def update(self):
        error = None
        success = False
        req_json = user.validRequest(request)
        if req_json != None and 'update' in req_json:
            username = req_json['username']
            update_dict = req_json['update']
            if update_dict:
                todo_key = get_todo_key(username)
                for todo_task in update_dict:
                    if redis_client.hexists(todo_key, todo_task):
                        redis_client.hset(todo_key, todo_task, update_dict[todo_task])
                        success = True
            else:
                error = "no update included"
        else:
            error = "invalid login"
        return jsonify({'success':success, 'error':error})

    def delete(self):
        error = None
        success = False
        deleted = []
        req_json = user.validRequest(request)
        if req_json != None and 'delete' in req_json:
            username = req_json['username']
            delete_list = req_json['delete']
            if len(delete_list) !=0:
                todo_key = get_todo_key(username)
                for todo_task in delete_list:
                    if redis_client.hdel(todo_key, todo_task):
                        deleted.append(todo_task)
                        if not success:
                            success = True
            else:
                error = "no deletion included"
        else:
            error = "invalid login"
        return jsonify({'success':success, 'error':error, 'deleted':deleted})


    def list_all(self):
        error = None
        todo_json = None
        json_req = request.get_json()
        req_json = user.validRequest(request)
        if req_json != None:
            todo_json = get_todo_dict(req_json['username']) 
        else:
            error = "invalid login"
        return jsonify({'todo':todo_json, 'error': error})



todo_item = Todo_Item()

