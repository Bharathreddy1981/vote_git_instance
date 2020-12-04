

def voter(db, updated_value, updated_token):
    #updated_value = ' ' + value + ' '
    #updated_token = ' ' + token + ' '
    cursor = db.cursor()

    query_id = "select * from election  where account_id = '" + str(updated_value) + "'"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4],
             "role_name": i[5], "token": i[6], "party_name":i[7],}
        login_list.append(k)
    print(login_list)



    query = "select * from election  where token = '" + str(updated_token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4],
             "role_name": i[5], "token": i[6], "party_name":i[7],}
        login_list11.append(k)
    print(login_list11)

    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}





    if login_list[0]["email"] == login_list11[0]["email"] and login_list[0]["account_id"] == login_list11[0]["account_id"]:
        if login_list[0]["role_name"] == "admin":
            cursor = db.cursor()
            try:
                query = "SELECT * FROM election "
                cursor.execute(query)
                data = cursor.fetchall()
                candidates_list = []
                for i in data:
                    k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4],
                         "role_name": i[5], "token": i[6], "party_name": i[7]}
                    candidates_list.append(k)

            except:
                return {'Error': 'id already existed'}
        else:
            return {" vote " : " enter the valid credentilas "}
    else:
        return {" vote ": " enter the valid credentilas "}

    return { "  number_of_vote "  : candidates_list}








