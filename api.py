import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

answers = [
    "Yes",
    "No",
    "Maybe",
    "You must be curious!"
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Persona Extractor</h1><p>This site is a prototype API for extracting persona sentences from a dialogue.</p>"

# A route to return all available answers
@app.route('/api/all', methods=['GET'])
def api_all():
    return answers

# A route to return one specific answer
@app.route('/api/reply', methods=['GET'])
def api_reply():
    nr = int(flask.request.args.get('nr', 0))
    if nr > 0 and nr <= len(answers):
        answer = answers[nr - 1]
    else:
        answer = "What do you mean?"
    return answer

# A route to return the square of a number
@app.route('/api/square', methods=['GET'])
def api_square():
    if 'nr' in flask.request.args:
        nr = float(flask.request.args['nr'])
        sq = nr * nr
        return f"<h1>Square</h1><p>The square of {nr} is {sq:.2f} (with two decimals)</p>"

    else:
        return "Square what?"                   

app.run(host="0.0.0.0", port=10000)