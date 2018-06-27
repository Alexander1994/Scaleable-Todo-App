
from flask import Flask
from app.views.user import user
from app.views.todo_item import todo_item

server = Flask(__name__)

@server.route('/login', methods=['POST'])
def login():
    return user.login()

@server.route('/logout', methods=['POST'])
def logout():
    return user.logout()

@server.route('/todo/list_all', methods=['POST'])
def create_todo():
    return todo_item.list_all()