import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB_NAME"),
)

print(db)

hos_name = "Seif  Hospital"
hos_code = "SH127"

cursor = db.cursor()
cursor.execute(f"""
    INSERT INTO hospital (hospital_name, hospital_code)
    VALUES ("{hos_name}", "{hos_code}")
""")
db.commit()

cursor.execute("SELECT * FROM hospital")
result = cursor.fetchall()
for row in result:
    print(row)

db.close()