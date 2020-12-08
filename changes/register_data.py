

from uuid import uuid4
def enter(db, data, encrypted_password):

    print(data)
    name = data["name"]
    phone = data["phone"]
    email = data["email"]
    passwd = data["password"]
    role_name = data["role_name"]

    if len(name) <= 3 or len(name) >= 15:
        return {'Error': 'range between 3-15'}
    elif phone == int(phone) and len(str(phone)) != 10:
        return {'Error': 'phone number must contain 10 digits'}
    elif len(email) <= 10 or len(email) >= 25:
        return {'Error': 'email range between 10-25'}
    elif len(passwd) <= 6 or len(passwd) >= 20:
        return {'Error': 'password range between 7-20'}

    try:
        cursor = db.cursor()
        query = "insert into vote (account_id, name, phone, email, password, role_name) values ('" + str(uuid4()) + "', '" + str(name) + "','" + str(phone) + "','" + str(email) + "','" + str(encrypted_password) + "','" + str(role_name) + "')"
        cursor.execute(query)
        db.commit()

        return {"value": "data registerd sucessfully"}
    except Exception as e:
        return {"error": str(e).replace("(1062","").replace("\"","").replace("'6587985578' ","").replace("('vote.phone'","").replace("for key","").replace("'vote.phone'","").replace(",","").replace(" )","")}







