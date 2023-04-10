import flask
import os
import string
import requests

app = flask.Flask(__name__)
a = 7
b = 13
ip = "172.17.0.2"

#Client code
@app.route('/')
def index():
    return flask.render_template('home.html', sum = add(a, b), diff = sub(a, b))

#RPC handling and client Stub
def add(a: int, b:int):
    data =  requests.get("http://" + ip + ":5000/add/" + str(a) + "/" + str(b)).json()["result"]
    print(data)
    return data

def sub(a: int, b:int):
    data =  requests.get("http://" + ip + ":5000/sub/" + str(a) + "/" + str(b)).json()["result"]
    print(data)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))

