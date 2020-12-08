
from vote import database_connection, password, register_data, login_data, getting_register_data, voting, track, admin, list
from flask import Flask, jsonify, request
from changes import password_change, register_data, log_in, getting, database_conn, password_encrypt,email_phone


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


@app.route ("/register", methods=['POST'])
def reg():
    json_data = request.get_json()
    db = database_conn.data()
    encrypted_password = password_encrypt.pass_encrypt(json_data)
    value = register_data.enter(db, json_data, encrypted_password)
    return jsonify(value)


@app.route("/log_in", methods=['POST'])
def token ():
    json_data = request.get_json()
    db = database_conn.data()
    final_data = getting.login_info(db, json_data)
    log_data = log_in.generate(db, final_data, json_data)
    return jsonify(log_data)


@app.route("/password/account_id=<value>", methods=['POST'])
def change(value):
    json_data = request.get_json()
    token = request.headers["log_key"]
    db = database_conn.data()
    change = password_change.change_password(value, token, db, json_data)
    return jsonify(change)


@app.route("/emailandphone/account_id=<value>", methods=['POST'])
def name(value):
    json_data = request.get_json()
    token = request.headers["log_key"]
    db = database_conn.data()
    changing = email_phone.rolename(value, token, db, json_data)
    return jsonify(changing)



if(__name__=="__main__"):
    app.run(host='0.0.0.0')

