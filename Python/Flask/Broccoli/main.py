from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
  page = ""
  f = open("broccoli.html","r")
  page = f.read()
  f.close()
  return page

app.run(host='0.0.0.0', port=8080)
