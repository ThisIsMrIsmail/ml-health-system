import os
import sqlite3
from Trash.create_db import query

def Database():
    try:
        db_path = 'database.db'
        if not os.path.exists(db_path):
            open(db_path, 'a')
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.executescript(query)
            conn.commit()
        else:
            conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        return e