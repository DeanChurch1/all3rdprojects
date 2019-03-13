#Simple GUI
#Demonstrates creating a window
from tkinter import *

#root window
root = Tk()

root.title("buttons program")
root.geometry("500x500")
root.configure(bg="blue")

mainframe = Frame(root)
mainframe.grid()
mainframe.configure(bg="green")

label = Label(mainframe, text="This is a button")
label.grid()


buttn1 = Button(mainframe, text="button 1")
buttn1.grid()
buttn1.configure(bg="pink")

buttn2 = Button(mainframe)
buttn2.grid()
buttn2.configure(text="button 2", bg = "pink")

buttn3 = Button(mainframe)
buttn3.grid()
buttn3["text"] = "button 3"
buttn3["bg"] = "yellow"
buttn3["fg"] = "purple"














#kick off the window's event loop
root.mainloop()

