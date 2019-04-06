from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/adduser', methods = ['GET'])
def adduser():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            username = request.args.get("uname")
            print("got args")
            firebase_api.addUser(uid, username)
            return jsonify({"status": "ok",
                            "uid": uid})
    except:
        return jsonify({"status": "error"})

@app.route('/userdata', methods = ['GET'])
def getUserData():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            return jsonify({"status": "ok",
                            "uid": uid,
                            "userData": firebase_api.getUser(uid)})
    except:
        return jsonify({"status": "error"})

@app.route('/adduserinv', methods = ['GET'])
def addUserInv():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            prodId = request.args.get("pid")
            firebase_api.addInv(uid, prodId)
            return jsonify({"status": "error",
    except:
        return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
