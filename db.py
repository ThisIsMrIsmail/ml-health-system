import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB_NAME"),
)

user_name = "Ismail Sherif"
user_code = "IS-0001"
user_gender = "Male"
user_username = "ismail"
user_password = "helloworld"
user_additional_info = "He is a senior cs student."

cursor = db.cursor()
cursor.execute(f"""
    INSERT INTO users (user_name, user_code, user_gender, user_username, user_password, user_additional_info)
    VALUES ("{user_name}", "{user_code}", "{user_gender}", "{user_username}", "{user_password}", "{user_additional_info}")
""")
db.commit()

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
for row in result:
    print(row)

db.close()