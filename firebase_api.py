import pyrebase

def addUser(uid, name):
  if(uid not in dict(db.child("user").get().val()).keys()):
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

def getProjDetail(pid):
  return db.child("project").child(pid).get().val()

def getPort(uid):
  lsProj = []
  invs = db.child("user").child(uid).child("inv").get().val()
  print(invs)
  allProj = listAllProj()
  allProj = allProj[1:]
  print(allProj)
  init = True
  tmp = {}
  for i in range(len(allProj)):
      tmp[str(allProj[i]["proj"])] = allProj[i]
  print()
  print(tmp)
  allProj = tmp
  print(invs)
  for inv in invs:
    if(init):
        init = False
        continue
    lsProj.append([allProj[inv[0]], inv[1]])
  return lsProj



config = {
  "apiKey": "AIzaSyA8gvXnhMyyPaBLgLm7_eHFfBQA0UrasVQ",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://uhack19-4c33e.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
  #"serviceAccount": "./uhack19-4c33e-firebase-adminsdk-g8kea-812e567000.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

