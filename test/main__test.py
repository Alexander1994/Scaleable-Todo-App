
"""
Make shift test fail just to ensure functionality continues to work while being updated
"""

import requests
import json

url = "http://127.0.0.1:5000/"

def send_json(urlext, json_dict, req_type):
    req_url = url+urlext
    req_t = req_type.lower()
    if (req_t == 'get'):
        r = requests.get(req_url, params=json_dict)
    elif (req_t == 'post'):
        r = requests.post(req_url, json=json_dict)
    return r.json()

login_dict = {
    "username":"admin@admin.co",
    "password":"secret"
}
login_resp = send_json('login', login_dict, 'POST')
print(login_resp)
sessionId = login_resp['sessionId']

create_json = {
    "username":"admin@admin.co",
    "sessionId": sessionId,
    "add": {
        "create update feature":"incomplete"
    }
}
create_resp = send_json('todo/add', create_json, 'POST')
print(create_resp)

update_json = {
    "username":"admin@admin.co",
    "sessionId": sessionId,
    "update": {
        "create update feature":"complete"
    }
}
update_resp = send_json('todo/update', update_json, 'POST')
print(update_resp)

list_json = {
    "username":"admin@admin.co",
    "sessionId": sessionId
}
list_resp = send_json('todo/list_all', list_json, 'POST')
print(list_resp)

logout_dict = {
    "username":"admin@admin.co",
    'sessionId': sessionId
}
logout_resp = send_json('logout', logout_dict, 'POST')
print(logout_resp)