

def total_votes(db, updated_value, updated_token, enter):
    cursor = db.cursor()

    query_id = "select * from election  where account_id = '" + str(updated_value) + "'"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6], "party_name":i[7]}
        login_list.append(k)

    query = "select * from election  where token = '" + str(updated_token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6], "party_name":i[7]}
        login_list11.append(k)


    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}



    if login_list[0]["email"] == login_list11[0]["email"] and login_list[0]["account_id"] == login_list11[0]["account_id"]:
        cursor = db.cursor()
        try:
            query = "SELECT * FROM election where name ='" + str(enter) + "'"
            cursor.execute(query)
            data = cursor.fetchall()
            candidates_list = []
            for i in data:
                k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4],
                     "role_name": i[5], "token": i[6],"party_name":i[7]}
                candidates_list.append(k)

        except:
            return {'Error': 'enter valid name'}
    else:
        return {" vote ": " enter the valid credentilas "}

    return { "voted_for "  : candidates_list}


