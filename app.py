import streamlit as st
from auth import login
from admin import admin_dashboard
from mentor import mentor_dashboard
from intern import intern_dashboard

st.set_page_config(page_title="Internship Management System")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

st.title("Role-Based Internship & Project Management System")

if not st.session_state.logged_in:
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        result = login(username, password)

        if result:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = result[0]
            st.rerun()
        else:
            st.error("Invalid credentials")

else:
    st.success(f"Logged in as {st.session_state.role}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.rerun()

    if st.session_state.role == "Admin":
        admin_dashboard()

    elif st.session_state.role == "Mentor":
        mentor_dashboard()

    elif st.session_state.role == "Intern":
        intern_dashboard(st.session_state.username)
