
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_todo_key(username):
    return "%s:todo".format(username)

def get_todo_dict(username):
    todo_key = "%s:todo".format(username)
    todo_byte_data = redis_client.hgetall(todo_key)
    todo_dict = {k.decode('utf-8'): v.decode('utf-8') for k,v in todo_byte_data.items()}
    print(type(todo_dict))

    print(todo_dict)
    return todo_dict


# Design
"""
session_storage_design = {
    'brittany@gmail.ca': {
        'sessionId': '1234',
        'timeout': '12'
    },
    'brittany@gmail.ca:todo': { # ":" in the E-mail spec it has to be wrapped in quotes which is not, so in possible to have duplicates :)
        'build house': 'half-way',
        'eat sandwich': 'complete'
    }
    ...
}
"""