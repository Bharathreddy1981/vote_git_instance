


def candidates(db, updated_value, token):
    #updated_value = ' '+value+' '
    #updated_token = ' '+token+' '

    cursor = db.cursor()

    query_id = "select * from election where account_id = ('"+str(updated_value)+"')"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password" : i[4], "role_name": i[5], "token" : i[6]}
        login_list.append(k)
    print(login_list)




    query = "select * from election  where token = '" + str(token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password" : i[4], "role_name": i[5], "token" : i[6]}
        login_list11.append(k)
    print(login_list11)



    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}
    else:
        return 'you can vote for the candidate by passing a value which has given below:', {'TRS': 1, 'BJP': 2, 'CONGRESS':3}


