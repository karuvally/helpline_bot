#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run, request
import os
from pymongo import MongoClient

mongoclient = MongoClient(os.environ.get('MONGO_HOST', 'localhost'))
helpline_db = mongoclient["helpline_db"]

# receive the phone number
@route("/upload")
def upload():
    pass
    # do the stuff

@route('/registration', method='POST')
def registration():
    try:
        volunteer = {
            'name': request.forms['name'],
            'phone_number': request.forms['phone'],
            'district': request.forms['district']
        }
    except KeyError:
        return "<p>Field missing.</p>"
    if helpline_db['volunteer'].find_one({'phone_number': volunteer['phone_number']}):
        return "volunteer already exists"
    helpline_db['volunteer'].insert_one(volunteer)
    return "volunteer added"

run(host="0.0.0.0", port = 8080, debug = True)