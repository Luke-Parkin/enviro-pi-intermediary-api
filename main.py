from flask import Flask, abort
from flask import request
import firebase_admin
from firebase_admin import db

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate("admin.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://enviro-pi-logger-default-rtdb.firebaseio.com/"})
ref = db.reference()

AUTH_TOKEN = "please-move-this-into-an-env-file"

@app.route("/", methods = ['POST'])
def enviro():
    if request.headers.get("Authorization") == f"Bearer {AUTH_TOKEN}":
        data = request.json
        ref.push(data)
        return "success",200
    else:
        return "unauthorised",401