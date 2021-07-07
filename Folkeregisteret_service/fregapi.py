from flask import Flask, request
from flask.json import jsonify
from fregservice import Person

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/batch", methods=['GET'])
def batch():
    if request.method == 'GET':
        person = Person()
        return jsonify(person.batch)
    

