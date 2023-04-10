import flask
import os
import string

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

#RPC handling and server stub
@app.route('/<string:op>/<int:a>/<int:b>')
def calc(op: string, a: int, b: int):
    if (op == "add"):
        return flask.jsonify({"result": add(a, b)}), 200
    elif (op == "sub"):
        return flask.jsonify({"result": sub(a, b)}), 200
    else: 
        return flask.jsonify({"Operation invalid": op}), 400


#Server implementations
def add(a: int, b: int):
    return a + b

def sub(a: int, b: int):
    return a - b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

