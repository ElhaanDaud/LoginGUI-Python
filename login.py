import streamlit as st
import mysql.connector as ms
import creds 
from pages.signup import signup  

# Establish connection to the MySQL database
m = ms.connect(host=creds.host, user=creds.user, password=creds.password, database=creds.database) 
cursor = m.cursor()

st.title("Login Page")

# Input fields for username and password
email = st.text_input("Username")
password = st.text_input("Password", type="password")

value = (email, password)
sql = "select * from auth where email = %s and password = %s"
cursor.execute(sql, value)
L = cursor.fetchall()

# Create two columns
col1, col2 = st.columns([1, 6])

# Add a button to the first column
with col1:
    login_button = st.button("Login")

# Add a button to the second column
with col2:
    signup_button = st.button("Signup")

# Button to submit the form
if login_button:
    # Dummy authentication logic (replace with your own authentication logic)
    if len(L) == 0:
        st.error("Invalid username or password")
    else:
        st.success("Login successful!")

# If signup button is clicked, navigate to the signup page
if signup_button:
    signup()  # Call the signup function

# Close the database connection
m.close()
