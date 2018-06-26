#!/usr/bin/env bash

user='postgres'
filename='setupdb.sql'

echo $(sudo psql -U $user -a -f $filename)
