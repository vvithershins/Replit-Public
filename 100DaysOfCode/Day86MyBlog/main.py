from flask import Flask, redirect, session, request
from replit import db
import os

#to set up you must create a db entry with the key "user" and the value being a dictionary with the keys "username" and "password" the values being your username and password you can use a secret for the password, then delete the secret
#db["user"] = {"username": "sampleusername", "password": os.environ["password"] or "samplepassword"}
#to delete an entry run the program to get the name of the key you want to delete and then run the program again and it will delete the key
"""for key in db.keys():
  print(key)
"""

"""for key in db.keys():
  if key == "2024-09-02 | 05:43":
    print("yes")
    del db[key]
    print("deleted entry")"""


app = Flask(__name__ , static_url_path ="/static")
app.secret_key = os.environ['secretKey']


def getBlogs():
  entry = ""
  f = open("entry.html", "r")
  entry = f.read()
  f.close()
  keys = db.keys()
  content = ""
  for key in sorted(db.keys(), key=lambda k: (db[k].get('date', ''), db[k].get('time', '')), reverse=True):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      thisEntry = thisEntry.replace("{time}" , db[key]["time"])
      content += thisEntry
  return content



@app.route('/')
def index():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{content}", getBlogs())
  return page

@app.route("/loginForm")
def loginForm():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/login' , methods=["POST"])
def login():
  if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] and form["password"] == db["user"]["password"]:
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route('/edit')
def edit():
  if not session.get("user"):
    return redirect("/")
  page = ""
  f = open("edit.html", "r")
  page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page

@app.route("/add" , methods=["POST"])
def add():
  form = request.form
  entry = {"title" : form["title"], "date": form["date"], "body": form["body"], "time": form["time"]}
  datetime = f"{form['date']} | {form['time']}"
  db[datetime] = entry
  return redirect("/edit")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)
