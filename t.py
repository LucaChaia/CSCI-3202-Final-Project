from tkinter import *

val = ""

def boardSetup(window):
    global val
    val = val + "1"
    print(val)
    window.mainloop()

window = Tk()
window.geometry('1000x600')

b = Button(window, text = "Test", command=boardSetup)
b.pack()