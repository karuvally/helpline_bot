#!/usr/bin/env python3
# The database bot, alpha release

# import serious stuff
from bottle import run, post, request


# read the just commited data
@post("/upload")
def get_data():
    pass


# initialize the program
# set up postgresql database