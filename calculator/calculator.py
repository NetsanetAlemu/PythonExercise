from tkinter import *
def a():
    wind = Tk()
    wind.geometry("400x500")
    wind.config(bg="#333300")
    lab = Label(wind, text="New page", fg="#dD3906", bg="#ff3", font=("Arial", 30))
    lab.place(x=100, y=100)
    wind.mainloop()
window = Tk()
window.config(bg="#930")
window.geometry("400x500")
home = Label(window, text="Home page", font=("Arial", 20), bg="#552200", fg="#ff00ff")
button = Button(window, text="save", command=a, bg="#330882", fg="#32220c", font=("Arial", 20))
home.place(x=130,y=100)
button.place(x=150,y=150)

window.mainloop()