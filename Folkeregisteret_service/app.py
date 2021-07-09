from flask import Flask, request
from flask.json import jsonify
from werkzeug.utils import escape
from fregservice import Person

app = Flask(__name__)

# powershell: 
# $env:FLASK_APP = path
# flask run

@app.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return escape("<p>This is the root :)</p>")

@app.route("/person", defaults={'personnummer': None}, methods=['GET'])
@app.route("/person/<personnummer>", methods=['GET'])
def person(personnummer):
    if request.method == 'GET':
        if personnummer is not None:
            personnummer = personnummer+".json"
        person = Person(file_name=personnummer)
        return jsonify(person.batch)


@app.route("/batch", methods=['GET'])
def single():
    if request.method == 'GET':
        number_of_available_people = Person().get_number_of_files_in_directory()

        all_people = [dict() for x in range(number_of_available_people)]
        for i in range (number_of_available_people):
            all_people[i] = Person(file_position_in_directory=i).batch
        return jsonify(all_people)
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
    
