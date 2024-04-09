from flask import Flask, request, redirect
import json

app = Flask(__name__, static_url_path="/static")

# Load the votes from a file or initialize an empty dictionary if the file doesn't exist
try:
    with open("votes.json", "r") as f:
        votes = json.load(f)
except FileNotFoundError:
    votes = {
        "one": 0,
        "two": 0,
        "neither": 0,
    }

@app.route('/')
def index():
    page = ""
    with open("template/blog.html", "r") as f:
        page = f.read()

    # Update the page to display the vote counts for each color
    page = page.replace("Which square is darker?", "Which square is darker? (Color 1 votes: {}, color 2 votes: {}, Neither : {})".format(votes["one"], votes["two"], votes["neither"]))
    return page

@app.route('/vote', methods=['GET'])
def vote():
    color = request.args.get('color')

    # Check if the color is valid
    if color in votes:
        votes[color] += 1

        # Save the updated votes to the file
        with open("votes.json", "w") as f:
            json.dump(votes, f)

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
