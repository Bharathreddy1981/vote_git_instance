

def votes(updated_value, db, updated_token, jsondata):
    #updated_value = ' ' + value + ' '
    #updated_token = ' ' + token + ' '
    cursor = db.cursor()

    query_id = "select * from election  where account_id = '" + str(updated_value) + "'"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6]}
        login_list.append(k)
    print(login_list)




    query = "select * from election  where token = '" + str(updated_token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name": i[5],
                 "token": i[6]}
        login_list11.append(k)
    print(login_list11)



    if len(login_list) == 0:
        return {'Error': "invalid voter_id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}


    bjp = jsondata["1"]
    #trs = jsondata["1"]
    #congress = jsondata["3"]
    print(bjp)


    if login_list[0]["email"] == login_list11[0]["email"] and login_list[0]["name"] == login_list11[0]["name"]  :

        cursor = db.cursor()
        try:
            query121 = "UPDATE election SET party_name = ' " + str(bjp) + " '"
            cursor.execute(query121)
            db.commit()
        except:
            return {'Error': 'enter the valid credentilas'}

    return { " vote "  : " you registed your vote sucessfully "}



