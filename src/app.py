"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, json, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def add_memberApp():
    request_body = request.data
    decoded_object = json.loads(request_body)
    print(decoded_object)
    jackson_family.add_memberDataStr(decoded_object)
    print("Incoming request with the following body", decoded_object)
    return jsonify(jackson_family.get_all_members()),200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_memberApp(id):
    for i in range (len(jackson_family.get_all_members())):
        if jackson_family.get_all_members()[i]["id"] == id:
            jackson_family.get_all_members().pop(i)
            break
    print("This is the position to delete: ",id)
    return jsonify(jackson_family.get_all_members()),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
