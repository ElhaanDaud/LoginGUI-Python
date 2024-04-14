import streamlit as st
import mysql.connector as ms
import creds 

def signup():
    # Establish connection to the MySQL database
    m = ms.connect(host=creds.host, user=creds.user, password=creds.password, database=creds.database) 
    cursor = m.cursor()

    # Function to register a new user
    def register(new_email, new_password):
        # Insert new user into the database
        value = (new_email, new_password)
        sql = "INSERT INTO auth VALUES (%s, %s)"
        cursor.execute(sql, value)
        m.commit()
        st.success("Successfully signed up!")

    st.title("Signup Page")

    # Input fields for username and password
    new_email = st.text_input("Enter your email")
    new_password = st.text_input("Enter your password", type="password")

    # Button to register
    if st.button("Signup",key="signup_button"):
        register(new_email, new_password)

    # Close the database connection
    m.close()


signup()