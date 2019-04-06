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
  
def addProj(proj, projName, hostName, status, vol):
  proj = {"proj": proj
        , "projName": projName
        , "hostName": hostName
        , "status": status
        , "vol": vol}
  db.child("/project/").child(proj).set(proj)

config = {
  "apiKey": "AIzaSyA8gvXnhMyyPaBLgLm7_eHFfBQA0UrasVQ",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://uhack19-4c33e.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
