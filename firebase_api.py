import pyrebase

def addUser(uid, name):
  data = {"uid": uid
        , "name": name
        , "inv": [0]}
  db.child("/user/").child(uid).set(data)

def getUser(uid):
  return db.child("user").child(uid).get().val()
    
def addInv(uid, proj, invest):
  data = getUser(uid)

  if(data == None):
      print("No user")
      return 0

  print("old data ->",data)
  data["inv"].append([proj, invest])
  updateVol(proj, invest)
  db.child("/user/").child(uid).set(data)


def updateVol(proj, invest):
  data = db.child("project").child(proj).get().val()
  data["cvol"] += int(invest)
  db.child("/project/").child(proj).set(data)

def listAllProj():
  return db.child("project").get().val()

def addProj(proj, projName, projInfo, projImg, hostName, status, cvol, vol):
  project = {"proj": proj
        , "projName": projName
        , "projInfo": projInfo
        , "projImg": projImg
        , "hostName": hostName
        , "status": status
        , "cvol" : cvol
        , "vol": vol}
  db.child("/project/").child(proj).set(project)

def getPort(uid):
  lsProj = []
  invs = db.child("user").child(uid).child("inv").get().val()
  allProj = listAllProj()
  for inv in invs:
    lsProj.append([allProj[inv[0]], inv[1]])
  return lsProj



config = {
  "apiKey": "AIzaSyA8gvXnhMyyPaBLgLm7_eHFfBQA0UrasVQ",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://uhack19-4c33e.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

