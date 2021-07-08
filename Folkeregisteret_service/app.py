from flask import Flask, request
from flask.json import jsonify
from fregservice import Person

app = Flask(__name__)

# powershell: 
# $env:FLASK_APP = path
# flask run

@app.route("/batch", methods=['GET'])
def batch():
    if request.method == 'GET':
        person = Person()
        return jsonify(person.batch)
    
if __name__ == "__main__":
    app.run(debug=True)