#!/usr/bin/env python3
# The database bot, alpha release

# import serious stuff
from bottle import run, post, request
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# setup essential variables
SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly"
RESCUE_SHEET_ID = "1womn9fd11hBCc3WFkxCf85WX6W9-Xcps7TvQZD57g9c"
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

    request = service.spreadsheets().values().get(spreadsheetId = RESCUE_SHEET_ID,
    range = RANGE)
    
    response = request.execute()
    
    for number in response["values"]:
        if number[0] == phone_number:
            return True
    
    return False


# read the just commited data
@post("/upload")
def handle_data():
    district = request.forms.get("district")
    location = request.forms.get("location")
    victim_name = request.forms.get("victim_name")
    victim_phone = request.forms.get("victim_phone")
    assigned_person = request.forms.get("assigned_person")

    victim_details.update({
        "district": district,
        "location": location,
        "victim_name": victim_name,
        "victim_phone": victim_phone,
        "assigned_person": assigned_person
        })
    # timestamp = # debug: generate timestamp
