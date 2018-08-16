#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run
from pymongo import MongoClient


# receive the phone number
@route("/upload")
def upload():
    pass
    # do the stuff


# the main function
def main():
    # setup MongoDB
    client = MongoClient()
    victim_database = client["victim_db"]

    # run the application
    run(host="0.0.0.0", port = 8080, debug = True)