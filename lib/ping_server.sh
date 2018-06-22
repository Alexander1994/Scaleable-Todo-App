#!/usr/bin/env bash

url="http://127.0.0.1:5000/login"
echo $(curl -X POST -H "Content-Type: application/json" -d '{"username":"admin@admin.co", "password":"secret"}' $url)
