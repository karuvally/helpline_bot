#!/usr/bin/env python3
# The database bot, alpha release

# import serious stuff
from bottle import run, post, request
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import requests


# essential varilables
victim_details = {}


# write entry to sheet
def write_to_sheet():
    url = "https://script.google.com/macros/s/AKfycbyirHH2K1rxt2Mhwe5xV9IJvenWVRfny7l64A7P/exec?From={}?Status={}?Comments={}".format(victim_details["victim_phone"],
    victim_details["assigned_person"], victim_details["comments"])
    requests.get(url)


# read the just commited data
@post("/upload")
def handle_data():
    victim_phone = request.forms.get("victim_phone")
    assigned_person = request.forms.get("assigned_person")
    comments = request.forms.get("comments")

    victim_details.update({
        "victim_phone": victim_phone,
        "assigned_person": assigned_person,
        "timestamp": time.strftime("%d/%b/%Y %H:%M:%S") # reference: 17/08/2018 00:15:33
        })
    
