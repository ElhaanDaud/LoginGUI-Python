import streamlit as st
import mysql.connector as ms
import creds 

m=ms.connect(host=creds.host, user=creds.user, password=creds.password, database=creds.database) 
cursor=m.cursor()


st.title("Login Page")

# Input fields for username and password
email = st.text_input("Username")
password = st.text_input("Password", type="password")

value=(email,password)
sql="select * from auth where email = %s and password = %s"
cursor.execute(sql,value)
L = cursor.fetchall()

# Button to submit the form
if st.button("Login"):
    # Dummy authentication logic (replace with your own authentication logic)
    if len(L)==0:
        st.error("Invalid username or password")
        
    else:
        st.success("Login successful!")

if st.button("Signup"):
    signup()

m.close()