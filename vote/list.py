


def candidates(db, updated_value, token):
    cursor = db.cursor()
    query_id = "select * from election where account_id = ('"+str(updated_value)+"')"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password" : i[4], "role_name": i[5], "token" : i[6]}
        login_list.append(k)

    query = "select * from election  where token = '" + str(token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password" : i[4], "role_name": i[5], "token" : i[6]}
        login_list11.append(k)

    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}
    else:
        return {"candidates" : "list of candidates present in the voting poll.if you want to vote for BJP type 1.if you want to vote for CONGRESS type 2.if you want to vote for TRS type 3."}


