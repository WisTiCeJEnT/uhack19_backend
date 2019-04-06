from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/adduser', methods = ['POST'])
def adduser():
    try:
        if request.method == 'POST':
            uid = request.args.get("uid")
            username = request.args.get("uname")
            print("got args")
            firebase_api.addUser(uid, username)
            return jsonify({"status": "ok"})
    except:
        return jsonify({"status": "error"})

@app.route('/userdata', methods = ['POST'])
def getUserData():
    try:
        if request.method == 'POST':
            uid = request.args.get("uid")
            return jsonify({"status": "ok", "userData": firebase_api.getUser(uid)})
    except:
        return jsonify({"status": "error"})

@app.route('/adduserinv', methods = ['POST'])
def addUserInv():
    try:
        if request.method == 'POST':
            uid = request.args.get("uid")
            prodId = request.args.get("pid")
            firebase_api.addInv(prodID, uid)
            return jsonify({"status": "ok"})
    except:
        return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
