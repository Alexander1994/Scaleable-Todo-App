#!/usr/bin/env bash

url="http://127.0.0.1:5000/logout"
hash="ccee9a49a922a44efb6b5769544865ec876c3ddf656bf0d250a94ddea400c4bd" # hashes no longer static...
username="admin@admin.co"
echo $(curl -X POST -H "Content-Type: application/json" -d "{\"sessionId\":\"$hash\", \"username\":\"$username\" }" $url)
