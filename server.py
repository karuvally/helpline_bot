#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run, request, template
import os
from pymongo import MongoClient
import time

mongoclient = MongoClient(os.environ.get('MONGO_HOST', 'localhost'))
helpline_db = mongoclient["helpline_db"]

# receive the phone number
@route("/upload/<phone_number>")
def upload(phone_number):
    victim_data = {
        "sl_no": current_count, # debug
        "phone": phone_number,
        "time": time.strftime("[%d-%b-%Y %H:%M:%S]"),
        "name": None,
        "district": None,
        "location": None,
        "help_type": None,
        "status": None,
        "remarks": None,
        "gps": None
    }
    
    victims.insert_one(victim_data)
    current_count += 1


# get victim's phone
@route("/get_victim")
def get_victim():
    pass

@route('/registration')
def registration():
    return template('registration')

@route('/registration', method='POST')
def do_registration():
    try:
        volunteer = {
            'name': request.forms['name'],
            'phone_number': request.forms['phone'],
            'district': request.forms['district']
        }
    except KeyError:
        return "<p>Field missing.</p>"
    if volunteers.find_one({'phone_number': volunteer['phone_number']}):
        return "volunteer already exists"
    volunteers.insert_one(volunteer)
    return "volunteer added"


# setup MongoDB
client = MongoClient()
database = client["helpline_db"]

victims = database.victims
volunteers = database.volunteers

# run the application
run(host="0.0.0.0", port = 8080, debug = True)