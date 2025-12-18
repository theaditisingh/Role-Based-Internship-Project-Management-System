import streamlit as st
import sqlite3

def admin_dashboard():
    st.subheader("Admin Dashboard")

    conn = sqlite3.connect("internship.db")
    cur = conn.cursor()

    st.write("Add User")

    username = st.text_input("Username", key="admin_add_username")
    password = st.text_input("Password", type="password", key="admin_add_password")
    role = st.selectbox("Role", ["Mentor", "Intern"])

    if st.button("Add User"):
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        st.success("User added successfully")

    st.write("All Users")
    data = cur.execute("SELECT username, role FROM users").fetchall()
    st.table(data)
