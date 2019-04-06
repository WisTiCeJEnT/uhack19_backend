import pyrebase

def addUser(uid, name):
  data = {"uid": uid
        , "name": name
        , "inv": [0]}
  db.child("/user/").child(uid).set(data)

def getUser(uid):
  return db.child("user").child(uid).get().val()
    
def addInv(uid, prod, quan):
  data = getUser(uid)

  if(data == None):
      print("No user")
      return 0

  print("old data ->",data)
  data["inv"].append(prod)
  db.child("/user/").child(uid).set(data)

def listAllProj():
  return db.child("project").get().val()

def addProj(proj, projName, projInfo, projImg, hostName, status, cvol, vol):
  proj = {"proj": proj
        , "projName": projName
        , "projInfo": projInfo
        , "projImg": projImg
        , "hostName": hostName
        , "status": status
        , "cvol" : cvol
        , "vol": vol}
  db.child("/project/").child(proj).set(proj)

def getPort(uid):
  lsProj = []
  invs = db.child("user").child(uid).child("inv").get().val()
  allProj = listAllProj()
  for inv in invs:
    lsProj.append(allProj[inv])
  return lsProj

config = {
  "apiKey": "AIzaSyA8gvXnhMyyPaBLgLm7_eHFfBQA0UrasVQ",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://uhack19-4c33e.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

