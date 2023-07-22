import json
import os
from flask import Flask, abort
from flask import request
import firebase_admin
from firebase_admin import db

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate(json.loads(os.environ.get("FIREBASEADMIN")))
firebase_admin.initialize_app(cred, {"databaseURL":"https://enviro-pi-logger-default-rtdb.firebaseio.com/"})
ref = db.reference()

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

@app.route("/", methods = ['POST'])
def enviro():
    try:
        print(request.headers.get("Authorization"))
        print(AUTH_TOKEN)
        if request.headers.get("Authorization") == f"Bearer {AUTH_TOKEN}":
            print("refpush")
            data = request.json
            ref.push(data)
            print("yo")
            return "success",200
        else:
            return "unauthorised",401
    except Exception as e:
        print("Error",e)
        abort(400)
        
    
if __name__ == '__main__':
    app.run(threaded=True, port=80)