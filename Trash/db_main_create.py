import os
import sqlite3
from Trash.create_db import main_query

if "database.db" in os.listdir():
    os.remove("database.db")
os.system("touch database.db")

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.executescript(main_query)

conn.commit()
conn.close()