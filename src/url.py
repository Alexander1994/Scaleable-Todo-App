
from flask import Flask
from views.user import user

server = Flask(__name__)

@server.route('/login', methods=['POST'])
def login():
    return user.login()
