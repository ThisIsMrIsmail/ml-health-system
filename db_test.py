import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB_NAME"),
)

cursor = db.cursor()
cursor.execute(f"""
    INSERT INTO hopistals (hospital_name, hospital_code, user_username, user_password)
    VALUES ("Ismail Sherif", "IS-7482", "ismail", "hello")
""")
print(cursor.fetchall())
db.commit()
# result = cursor.fetchall()
# for row in result:
#     print(row)

db.close()