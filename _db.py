import os
import sqlite3

def Database():
    conn = sqlite3.connect('database.db')
    return conn