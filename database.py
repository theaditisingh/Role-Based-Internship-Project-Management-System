import sqlite3

def get_connection():
    return sqlite3.connect("internship.db", check_same_thread=False)

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern TEXT,
    task TEXT,
    status TEXT,
    marks INTEGER,
    remarks TEXT
)
""")

conn.commit()
conn.close()
