import streamlit as st
import sqlite3

def mentor_dashboard():
    st.subheader("Mentor Dashboard")

    conn = sqlite3.connect("internship.db")
    cur = conn.cursor()

    intern = st.text_input("Intern Username")
    task = st.text_area("Task Description")

    if st.button("Assign Task"):
        cur.execute(
            "INSERT INTO tasks (intern, task, status) VALUES (?, ?, ?)",
            (intern, task, "Assigned")
        )
        conn.commit()
        st.success("Task assigned")

    st.write("Evaluate Tasks")
    tasks = cur.execute("SELECT * FROM tasks").fetchall()
    for t in tasks:
        st.write(t)
