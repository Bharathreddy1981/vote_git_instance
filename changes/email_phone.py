

def rolename(value, token, db, data):
    email = data["email"]
    phone = data["phone"]
    name = data["name"]
    role = data["role_name"]

    if len(name) <= 3 or len(name) >= 15:
        return {'Error': 'range between 3-15'}
    elif len(email) <= 10 or len(email) >= 25:
        return {'Error': 'email range between 10-25'}
    elif len(str(phone)) != 10:
        return {'Error': 'phone number must contain 10 digits'}


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
        return {'Error': "invalid id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}

    if login_list[0]["name"] == login_list11[0]["name"] and login_list[0]["account_id"] == login_list11[0]["account_id"]:
        try:
            query = " UPDATE vote SET email = ('" + str(email) + "'), phone = ('" + str(phone) + "'), name =('" + str(name) + "'), role_name =('" + str(role) + "')  where account_id = '" + str(value) + "'"
            cursor.execute(query)
            db.commit()

        except:
            return {'Error': "email  and phone already exists "}

    else:
        return {" vote ": " enter the valid credentilas "}


    return {"value": "changed your name, email, rolename and phonenumber sucessfully"}



