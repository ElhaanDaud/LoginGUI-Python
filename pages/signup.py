def signup():
    def register():
        new_email = signup_username_entry.get()
        new_password = signup_password_entry.get()
        
        value=(new_email,new_password)
        sql="insert into auth values(%s,%s)"
        cursor.execute(sql,value)
        messagebox.showinfo("yay bitches!!","Successfully signed up!!")
        signup_window.destroy()
