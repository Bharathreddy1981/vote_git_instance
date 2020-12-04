
import jwt
import datetime
from vote import password
from flask import make_response


JWT_SECRET_KEY = 'thisisthesecretkey'
def generate_token(db, final_data, jsondata):

    email1 = jsondata["email"]
    passwd1 = jsondata["password"]
    #print(final_data)
    #password_check_final = password.pass_check(final_data[0]["password"], passwd1)  # generate true or false
    if len(final_data) == 0:
        return {"error": "invalid email"}

    elif email1 == final_data[0]["email"] :
        password_check_final = password.pass_check(final_data[0]["password"], passwd1)
        if  password_check_final == True:
            token1 = jwt.encode(
                { 'username': email1, 'password': passwd1 ,'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)},
            JWT_SECRET_KEY
                )
            token = token1.decode('UTF-8')
            cursor = db.cursor()
            query = "UPDATE election SET token = '" + str(token) + "'"

            cursor.execute(query)
            db.commit()



            query1 = "select * from election where email='" + str(email1) + "'"
            cursor.execute(query1)
            data = cursor.fetchall()
            log_list = []
            for i in data:
                k = {"account_id": i[0], "name": i[1], "phone": i[2], "email": i[3], "password" : i[4],"role_name":i[5], "token" : i[6]}
                log_list.append(k)

            if len(log_list) == 0:
                return { "error" : "invalid user or password"}
            else:
                return {"token" : token, "id" :log_list[0]["account_id"], "candidates":"list of candidates present in the voting poll.if you want to vote for BJP type 1.if you want to vote for CONGRESS type 2.if you want to vote for TRS type 3."}
        else:
            return {"error": "invalid  password"}
    else:
        return {"error": "invalid email"}


    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})



