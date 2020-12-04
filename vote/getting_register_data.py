def login_info(db, value):
    email = value["email"]

    cursor = db.cursor()
    w = "select * from election where email = '" + str(email) + "'"
    cursor.execute(w)
    bha = cursor.fetchall()

    login_email = []
    for i in bha:
        k = {"account_id" : i[0],"name": i[1], "phone": i[2], "email": i[3], "password": i[4], "role_name":i[5]}
        login_email.append(k)

    return  login_email




