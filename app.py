
from vote import database_connection, password, register_data, login_data, getting_register_data, voting, track, admin, list
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route("/register_data", methods=['POST'])
def register():
    json_data = request.get_json()
    db = database_connection.data()
    encrypted_password = password.pass_encrypt(json_data)
    value = register_data.inserting(db, json_data, encrypted_password)
    return jsonify(value)


@app.route("/login_data", methods=['POST'])
def login():
    json_data = request.get_json()
    db = database_connection.data()
    final_data = getting_register_data.login_info(db, json_data)
    log_data = login_data.generate_token(db, final_data, json_data)
    return jsonify(log_data)


@app.route("/candidates/voter_id=<value>", methods=['GET'])
def candi(value):
    token = request.headers["log_key"]
    db = database_connection.data()
    name = list.candidates(db, value, token)
    return  {"candidates":name}



@app.route ("/vote/<value>",  methods=['POST'])
def vote(value):
    token = request.headers["log_key"]
    json_data = request.get_json()
    db = database_connection.data()
    voted = voting.votes(value, db, token, json_data)
    return jsonify(voted)



@app.route ("/total/login_id=<value>/<name>",  methods=['GET'])
def final(value, name):
    db = database_connection.data()
    token = request.headers["log_key"]
    result = track.total_votes(db, value, token, name)
    return jsonify(result)


@app.route ("/result/login_id=<values>",  methods=['GET'])
def result(values):
    db = database_connection.data()
    token = request.headers["log_key"]
    resulted = admin.voter(db, values, token)
    return jsonify(resulted)



if(__name__=="__main__"):
    app.run(debug='0.0.0.0')

