
from flask import Flask
from app.views.user import user
from app.views.todo_item import todo_item

server = Flask(__name__)

# User
@server.route('/login', methods=['POST'])
def login():
    return user.login()

@server.route('/logout', methods=['POST'])
def logout():
    return user.logout()

# Todo
@server.route('/todo/list_all', methods=['POST'])
def list_all_todo():
    return todo_item.list_all()

@server.route('/todo/add', methods=['POST'])
def add_todo():
    return todo_item.add()

@server.route('/todo/update', methods=['POST'])
def update_todo():
    return todo_item.update()

@server.route('/todo/delete', methods=['POST'])
def delete_todo():
    return todo_item.delete()