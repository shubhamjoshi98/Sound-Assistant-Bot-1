from tkinter import *
import os
window=Tk()
window.title("My Assistant")

photo1= PhotoImage(file="./gallery/pic2.gif")
Label(window,image=photo1,bg="black").grid(row=0,column=0,sticky=E)

def run():
    os.system('python ./project1.py')


btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
btn.grid(column=0, row=4)


window.mainloop()