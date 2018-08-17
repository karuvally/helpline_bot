#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run, request, template
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

# get last unprocessed victim id
def get_unprocessed_victim():
    result = counter.find_one({"id": "counter"})
    last_unprocessed = int(result["last_unprocessed"])
    return last_unprocessed

# receive the phone number
@route("/upload/<data_string>")
def upload(data_string):
    splitted_string = data_string.split("&")
    for string in splitted_string:
        if string.find("From") != -1:
            phone_number = string.split("=")[1]
    
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
    current_count += 1


# get victim's phone
@route("/get_form")
def get_form():
    unprocessed_victim_id = get_unprocessed_victim()
    return victim_details.html
    #counter.update_one({"id": "counter"}, {'$inc': {"last_unprocessed": 1}})


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
counter = database.counter


# initialize counter
if not os.path.exists("counter.lock"):
    counter.insert_one({"id": "counter", "counter": 0, "last_processed": 0})
    with open("counter.lock", "w") as lock_file:
        lock_file.write("LOCKED")

get_count() # debug

# run the application
run(host="0.0.0.0", port = 8080, debug = True)