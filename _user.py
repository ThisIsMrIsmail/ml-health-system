
import random
import string

# ------------------------------------------------------
# _user.py,used in app.py, contains the functions for the user endpoints.
#
# The functions are:
#   - Register(data, db)
#   - Login(data, db)
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

def Register(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT * FROM users
        WHERE user_username = '{data["user_username"]}'
    """)
    response = cursor.fetchall()
    if len(response) >= 1:
        db.close()
        print("Response Data Sent:", {"message": "Username already exists", "auth": False})
        return {"message": "Username already exists", "auth": False}, 400
    # User Code ex: IS-7482
    code = ''.join(random.choice(string.digits) for i in range(4))
    data["user_code"] = f"{data['user_name'][:2].upper()}-{code}"
    cursor.execute(f"""
        INSERT INTO users (
            user_name, user_code, user_gender,
            user_username, user_password,
            user_additional_info, hospital_id)
        VALUES (
            '{data["user_name"]}', '{data["user_code"]}', '{data["user_gender"]}',
            '{data["user_username"]}', '{data["user_password"]}',
            '{data["user_additional_info"]}', '{data["hospital_id"]}')
    """)
    db.commit()
    db.close()
    print("Response Data Sent:", {"message": "User registered successfully"})
    return {"message": "User registered successfully", "auth": True}, 200

# ------------------------------------------------------

def Login(data, db):
    print("Request Data Recieved:", data)
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT * FROM users
        WHERE user_username = '{data["user_username"]}'
        AND user_password = '{data["user_password"]}'
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
