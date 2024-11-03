import os
import mysql.connector

def Database():
    conn = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB_NAME"),
    )
    return conn
