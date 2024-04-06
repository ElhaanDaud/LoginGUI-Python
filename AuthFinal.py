import tkinter as tk
from tkinter import messagebox
import mysql.connector as ms

m = ms.connect(host="localhost", user='root', password='SQL#pass#dora', database='login_info')
cursor = m.cursor()

def login():
    email = email_entry.get()
    password = password_entry.get()
    value = (email, password)
    sql = "select * from auth where email = %s and password = %s"
    cursor.execute(sql, value)
    L = cursor.fetchall()
    if len(L) == 0:
        messagebox.showerror("Error", "Invalid credentials", bg="blue", fg="white")  # Adjust message box color
    else:
        messagebox.showinfo("Success", "Successfully logged in!", bg="blue", fg="white")  # Adjust message box color

def signup():
    def register():
        new_email = signup_username_entry.get()
        new_password = signup_password_entry.get()
        value = (new_email, new_password)
        sql = "insert into auth values(%s,%s)"
        cursor.execute(sql, value)
        messagebox.showinfo("Success", "Successfully signed up!!", bg="blue", fg="white")  # Adjust message box color
        signup_window.destroy()

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    signup_username_label = tk.Label(signup_window, text="Username", bg="#FFA07A", fg="white")
    signup_username_label.pack()
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.pack()

    signup_password_label = tk.Label(signup_window, text="Password", bg="#FFA07A", fg="white")
    signup_password_label.pack()
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.pack()

    signup_button = tk.Button(signup_window, text="Sign Up", command=register)
    signup_button.pack()

root = tk.Tk()
root.title("Authorisation Window")

email_label = tk.Label(root, text="Email", bg="#FFA07A", fg="white")
email_label.pack(padx=10, pady=2)
email_entry = tk.Entry(root)
email_entry.pack(padx=100, pady=20)

password_label = tk.Label(root, text="Password", bg="brown", fg="white")
password_label.pack(padx=100, pady=2)
password_entry = tk.Entry(root, show="*")
password_entry.pack(padx=10, pady=2)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(padx=10, pady=2)

signup_button = tk.Button(root, text="Sign Up", command=signup)
signup_button.pack(padx=10, pady=20)

root.configure(bg='light blue')
root.mainloop()

m.commit()
cursor.close()
m.close()
