import hashlib
from db import get_connection

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def validate_login(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    query = """
    SELECT role FROM users
    WHERE username = %s AND password = %s
    """
    cursor.execute(query, (username, hashed_password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return None
