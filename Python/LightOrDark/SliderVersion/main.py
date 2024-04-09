from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load initial skin tone data
with open('skin_tone_data.json', 'r') as f:
    skin_tone_data = json.load(f)

@app.route('/')
def index():
  page = ""
  with open("template/index.html", "r") as f:
      page = f.read()
      return page

@app.route('/vote', methods=['POST'])
def vote():
    vote_value = request.form['vote']
    # Save vote to JSON file
    with open('votes.json', 'a') as f:
        f.write(json.dumps({'vote': vote_value}) + '\n')
    return jsonify({'success': True})



app.run(host='0.0.0.0', port=81)
