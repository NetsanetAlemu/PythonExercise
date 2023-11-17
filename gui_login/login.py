from tkinter import *

def login():
    user_name = entry_uname.get()
    pass_word = entry_passw.get()
    print("User name: " + user_name)
    print("Pass word: " + pass_word)

window = Tk()

window.geometry("500x600")
window.title("Log in")
window.maxsize(width=500, height=600)

icon = PhotoImage(file='logo.png')

window.iconphoto(True, icon)
window.config(bg="#011515")

label_login = Label(window,
              text = "Log in",
              font=("Arial", 16),
              fg="#fff",
              bg="#011C1C",
              padx=20,
              pady=20,
              width=20
              )
label_uname = Label(window,
              text = "User name: ",
              font=("Arial", 16),
              fg="#fff",
              bg="#011515",
              padx=20,
              pady=20,
              )
label_passw = Label(window,
              text = "Password: ",
              font=("Arial", 16),
              fg="#fff",
              bg="#011515",
              padx=20,
              pady=20,
              )
entry_uname= Entry(window, 
                   font=("Arial", 14),
                   fg= "#00031C",
                   bg="#fff")
entry_passw = Entry(window, 
                   font=("Arial", 14),
                   fg= "#00031C",
                   bg="#fff",
                   show="*")
button_login = Button(window,
                      text="Log in",
                      font=("Arial", 14),
                      fg="#fff",
                      bg="#011C1C",
                      activebackground="#033B3B",
                      activeforeground="#fff",
                      command=login
                      )

label_login.place(x=100, y=100)
label_uname.place(x=10, y=200)
label_passw.place(x=10, y=260)
entry_uname.place(x=150, y=220)
entry_passw.place(x=150, y=280)
button_login.place(x=190, y=350)



window.mainloop()