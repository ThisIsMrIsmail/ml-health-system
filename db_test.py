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
cursor.execute()
db.commit()
print(cursor.fetchall())

db.close()