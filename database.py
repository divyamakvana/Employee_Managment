import sqlite3

def connect_db():
    return sqlite3.connect("employee.db")

def initialize_db():
    with connect_db() as conn:
        with open("schema.sql") as f:
            conn.executescript(f.read())
