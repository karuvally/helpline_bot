#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run, request
import os
from pymongo import MongoClient
import time

# mongoclient = MongoClient(os.environ.get('MONGO_HOST', 'localhost'))
# helpline_db = mongoclient["helpline_db"]

# maintain the counter
def get_count():
    result = counter.find_one({"id": "counter"})
    counter_value = int(result["counter"])
    
    counter.update_one({"id": "counter"}, {'$inc': {"counter": 1}})
    return counter_value

# receive the phone number
@route("/upload/<phone_number>")
def upload(phone_number):
    victim_data = {
        "sl_no": get_count(),
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


# get victim's phone
@route("/get_victim")
def get_victim():
    pass


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
    if database['volunteers'].find_one({'phone_number': volunteer['phone_number']}):
        return "volunteer already exists"
    database['volunteers'].insert_one(volunteer)
    return "volunteer added"


# setup MongoDB
client = MongoClient()
database = client["helpline_db"]

victims = database.victims
volunteers = database.volunteers
counter = database.counter

# initialize counter
if not os.path.exists("counter.lock"):
    counter.insert_one({"id": "counter", "counter": 0})
    with open("counter.lock", "w") as lock_file:
        lock_file.write("LOCKED")

get_count() # debug

# run the application
#run(host="0.0.0.0", port = 8080, debug = True)