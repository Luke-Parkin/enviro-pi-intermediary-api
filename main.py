import json
import os
from flask import Flask, abort
from flask import request
import firebase_admin
from firebase_admin import db

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate(os.environ.get(json.loads("FIREBASEADMIN")))
firebase_admin.initialize_app(cred, {"databaseURL":"https://enviro-pi-logger-default-rtdb.firebaseio.com/"})
ref = db.reference()

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

@app.route("/", methods = ['POST'])
def enviro():
    if request.headers.get("Authorization") == f"Bearer {AUTH_TOKEN}":
        data = request.json
        ref.push(data)
        return "success",200
    else:
        return "unauthorised",401