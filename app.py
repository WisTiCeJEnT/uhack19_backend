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
            return jsonify({"status": "ok",
                            "uid": uid})
    except:
        return jsonify({"status": "error"})

@app.route('/allproject', methods = ['GET'])
def listAllProject():
    if request.method == 'GET':
        allProj = firebase_api.listAllProj()
        print(allProj)
        tmp = []
        for i in range(1,len(allProj)):
            t = {}
            t["projID"] = allProj[i]["proj"]
            t["projName"] = allProj[i]["projName"]
            t["projDetail"] = allProj[i]["projInfo"]
            t["cVol"] = allProj[i]["cvol"]
            t["maxVol"] = allProj[i]["vol"]
            t["hostname"] = allProj[i]["hostName"]
            t["imglink"] = allProj[i]["projImg"]
            tmp.append(t)
        return jsonify({"status": "ok",
                        "projId": tmp})

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
