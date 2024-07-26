import json
import os
from flask import Flask, abort
from flask import request
import firebase_admin
from firebase_admin import db

import requests

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate(json.loads(os.environ.get("FIREBASEADMIN")))
firebase_admin.initialize_app(cred, {"databaseURL":"https://enviro-pi-logger-default-rtdb.firebaseio.com/"})
ref = db.reference()

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

@app.route("/", methods = ['POST'])
def enviro():
    try:
        auth = request.authorization
        if auth.password == AUTH_TOKEN:
            data = request.json
            ref.push(data)
            return "success",200
        else:
            return "unauthorised",401
    except Exception as e:
        print("Error",e)
        abort(400)
        
    
if __name__ == '__main__':
    app.run(threaded=True, port=80)