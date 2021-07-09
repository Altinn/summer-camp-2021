from flask import Flask, request
from flask.json import jsonify
from fregservice import Person

app = Flask(__name__)

# powershell: 
# $env:FLASK_APP = path
# flask run

@app.route("/batch", defaults={'personnummer': None}, methods=['GET'])
@app.route("/batch/<personnummer>", methods=['GET'])
def batch(personnummer):
    if request.method == 'GET':
        if personnummer is not None:
            personnummer = personnummer+".json"
        person = Person(file_name=personnummer)
        return jsonify(person.batch)
    
if __name__ == "__main__":
    app.run(debug=True)