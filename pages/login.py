def login():
    email = email_entry.get()
    password = password_entry.get()
    value=(email,password)
    sql="select * from auth where email = %s and password = %s"
    cursor.execute(sql,value)
    L = cursor.fetchall()
    if len(L)==0:
        messagebox.showerror("you suck =p","Not the correct credentials")
    else:
        messagebox.showinfo("yay bitches!!","Successfully logged in!")
