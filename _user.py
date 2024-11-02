def Login(data, db):
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT * FROM users
        WHERE user_username = '{data["username"]}'
        AND user_password = '{data["password"]}'
    """)
    response = cursor.fetchall()
    db.close()
    if len(response) == 0:
        return {"message": "Invalid credentials", "auth": False}, 401
    else:
        return {"message": "Login successful", "auth": True}, 200