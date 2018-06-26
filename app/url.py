
from flask import Flask
from app.views.user import user

server = Flask(__name__)

@server.route('/login', methods=['POST'])
def login():
    return user.login()

@server.route('/logout', methods=['POST'])
def logout():
    return user.logout()