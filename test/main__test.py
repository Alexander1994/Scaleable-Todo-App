
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

logout_dict = {
    "username":"admin@admin.co",
    'sessionId': login_resp['sessionId']
}
print(logout_dict)
logout_resp = send_json('logout', logout_dict, 'POST')
print(logout_resp)