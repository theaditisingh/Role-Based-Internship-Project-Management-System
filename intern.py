import streamlit as st
import sqlite3

def intern_dashboard(username):
    st.subheader("Intern Dashboard")

    conn = sqlite3.connect("internship.db")
    cur = conn.cursor()

    tasks = cur.execute(
        "SELECT id, task, status FROM tasks WHERE intern=?",
        (username,)
    ).fetchall()

    for t in tasks:
        st.write(t)
