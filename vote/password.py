from werkzeug.security import generate_password_hash, check_password_hash


def pass_encrypt(data):
    passwd = data["password"]
    hashed_password = generate_password_hash(passwd, method="sha256")

    return hashed_password


def pass_check(fetched_password, passwd):
    password_check_final = check_password_hash(fetched_password, passwd)
    return password_check_final
