# ------------------------------------------------------
# _user.py,used in app.py, contains the functions for the user endpoints.
#
# The functions are:
#   - Login(data, db)
#   - Register(data, db)
#   - Profile(data, db)
#   - Update(data, db)
#   - Delete(data, db)
#
# The functions take in two parameters:
#   - data: a dictionary containing the request data
#   - db: a connection to the database
#
# The functions return a tuple containing:
#   - a dictionary containing the response data
#   - an integer representing the status code
#
# The functions are used in app.py to handle the user endpoints.
# ------------------------------------------------------

def Login(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT * FROM users
        WHERE user_username = '{data["username"]}'
        AND user_password = '{data["password"]}'
    """)
    response = cursor.fetchall()
    db.close()
    if len(response) == 0:
        print("Response Data Sent:", {"message": "Invalid credentials", "auth": False})
        return {"message": "Invalid credentials", "auth": False}, 401
    else:
        print("Response Data Sent:", {"message": "Login successful", "auth": True})
        return {"message": "Login successful", "auth": True}, 200

# ------------------------------------------------------

def Register(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        INSERT INTO users (user_username, user_password)
        VALUES ('{data["username"]}', '{data["password"]}')
    """)
    db.commit()
    db.close()
    print("Response Data Sent:", {"message": "User registered successfully"})
    return {"message": "User registered successfully"}, 200

# ------------------------------------------------------

def Profile(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT * FROM users
        WHERE user_username = '{data["username"]}'
        AND user_password = '{data["password"]}'
    """)
    response = cursor.fetchall()
    db.close()
    if len(response) == 0:
        print("Response Data Sent:", {"message": "Invalid credentials", "auth": False})
        return {"message": "Invalid credentials", "auth": False}, 401
    else:
        print("Response Data Sent:", {"message": "Profile fetched successfully", "auth": True})
        return {"message": "Profile fetched successfully", "auth": True}, 200
    
# ------------------------------------------------------

def Update(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        UPDATE users
        SET user_username = '{data["new_username"]}',
        user_password = '{data["new_password"]}'
        WHERE user_username = '{data["username"]}'
        AND user_password = '{data["password"]}'
    """)
    db.commit()
    db.close()
    print("Response Data Sent:", {"message": "User updated successfully"})
    return {"message": "User updated successfully"}, 200

# ------------------------------------------------------

def Delete(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        DELETE FROM users
        WHERE user_username = '{data["username"]}'
        AND user_password = '{data["password"]}'
    """)
    db.commit()
    db.close()
    print("Response Data Sent:", {"message": "User deleted successfully"})
    return {"message": "User deleted successfully"}, 200

# ------------------------------------------------------