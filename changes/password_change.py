


from changes import password_encrypt
def change_password(value, token, db, json_data):
    old = json_data["password"]
    new = json_data["new_password"]
    reenter = json_data["confirm_password"]
    if len(new) <= 6 or len(new) >= 20:
        return {'Error': 'new password range between 7-20'}
    if len(reenter) <= 6 or len(reenter) >= 20:
        return {'Error': 'confirm password range between 7-20'}

    cursor = db.cursor()
    query_id = "select * from vote  where account_id = '" + str(value) + "'"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6]}
        login_list.append(k)

    query = "select * from vote  where token = '" + str(token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6]}
        login_list11.append(k)

    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}

    password = login_list[0]["password"]
    print(password)
    print(login_list[0]["name"])

    if login_list[0]["email"] == login_list11[0]["email"] and login_list[0]["account_id"] == login_list11[0]["account_id"]:

        password_check_final = password_encrypt.pass_check(password,old)
        if password_check_final == True:
            if new == reenter:
                new_encrpyt = password_encrypt.pass1_encrypt(new)
                print(new_encrpyt)
                cursor = db.cursor()
                query11 = "UPDATE vote SET password = '" + str(new_encrpyt) + "' where name = '" + str(login_list[0]["name"]) + "' "
                cursor.execute(query11)
                db.commit()
                data = cursor.fetchall()
                log_list = []
                for i in data:
                    k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4],
                     "role_name": i[5], "token": i[6]}
                    log_list.append(k)
                    print(log_list)
            else:
                return {"error": " password enter does not match each other"}
        else:
            return {"error": "invalid  old password"}
    else:
        return {" vote ": " enter the valid credentilas "}

    return { "value" : "changed your password sucessfully"}


