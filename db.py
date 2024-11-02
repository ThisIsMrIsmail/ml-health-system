import os
import mysql.connector

def create_conn():
    db = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB_NAME"),
    )
    return db

# cursor.execute(f"""
# """)
# db.commit()

# result = cursor.fetchall()
# for row in result:
#     print(row)

# db.close()