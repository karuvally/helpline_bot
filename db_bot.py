#!/usr/bin/env python3
# The database bot, alpha release

# import serious stuff
from bottle import run, post, request
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time


# setup essential variables
SCOPES = "https://www.googleapis.com/auth/spreadsheets"
#RESCUE_SHEET_ID = "1womn9fd11hBCc3WFkxCf85WX6W9-Xcps7TvQZD57g9c"
DUMMY_SHEET_ID = "1yFXR5IQ5gmaTPmWxQO5KcxRpmQ3tAOU43u3KxrFfeNc"
victim_details = {}


# write entry to sheet
def write_to_sheet(phone_number, assigned_person):
    # setup API
    store = file.Storage("token.json")
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    
    service = build("sheets", "v4", http = creds.authorize(Http()))


# read the just commited data
@post("/upload")
def handle_data():
    victim_phone = request.forms.get("victim_phone")
    assigned_person = request.forms.get("assigned_person")

    victim_details.update({
        "victim_phone": victim_phone,
        "assigned_person": assigned_person,
        "timestamp": time.strftime("%d/%b/%Y %H:%M:%S") # reference: 17/08/2018 00:15:33
        })
    
