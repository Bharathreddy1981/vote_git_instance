def login_info(db, value):
    email = value["email"]
    #password = value["password"]

    cursor = db.cursor()
    w = "select * from vote where email = '" + str(email) + "'"
    cursor.execute(w)
    bha = cursor.fetchall()

    login_email = []
    for i in bha:
        k = {"account_id" : i[0],"name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name":i[5]}
        login_email.append(k)
    #print(login_email)

    #if len(login_email) == 0:
     #   return {"error": "invalid email"}


    #print(login_email)

    return  login_email
