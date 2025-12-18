import sqlite3

def login(username, password):
    conn = sqlite3.connect("internship.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cur.fetchone()
    conn.close()
    return result
