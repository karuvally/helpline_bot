#!/usr/bin/env python3
# The database bot, alpha release

# import serious stuff
from bottle import run, post, request


# read the just commited data
@post("/upload")
def get_data():
    district = request.forms.get("district")
    location = request.forms.get("location")
    victim_name = request.forms.get("victim_name")
    victim_phone = request.forms.get("victim_phone")
    # timestamp = # debug: generate timestamp



# initialize the program
# set up postgresql database