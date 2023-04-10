import flask
import os
import string

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/<string:op>/<int:a>/<int:b>')
def calc(op: string, a: int, b: int):
    if (op == "add"):
        return flask.jsonify({"result": a + b}), 200
    elif (op == "sub"):
        return flask.jsonify({"result": a - b}), 200
    else: 
        return flask.jsonify({"Operation invalid": op}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

