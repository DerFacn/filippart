from bcrypt import gensalt, hashpw, checkpw


def generate_hash(password: str) -> str:
    salt = gensalt()
    password_bytes = password.encode('utf-8')
    password_hash = hashpw(password_bytes, salt)
    return password_hash.decode('utf-8')


def check_password(password: str, password_hash: str) -> bool:
    password_bytes = password.encode('utf-8')
    return checkpw(password_bytes, password_hash.encode('utf-8'))
