import pyrebase

def addUser(uid, name):
  data = {"uid": uid
        , "name": name}
  db.child("/user/").child(uid).set(data)

def getUser(uid):
  return db.child("user").child(uid).get().val()
    

config = {
  "apiKey": "AIzaSyA8gvXnhMyyPaBLgLm7_eHFfBQA0UrasVQ",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://uhack19-4c33e.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
