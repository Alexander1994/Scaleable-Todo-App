
from server import server, server_engine

@server.route('/login', methods=['POST'])
def root():
    return server_engine.login()
