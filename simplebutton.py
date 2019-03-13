from tkinter import*


class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create buttons that don't do anything"""
        self.label = Label(self, text="this is a button")
        self.label.grid()

        #1st button
        self.buttn1 = Button(self, text="button 1")
        self.buttn1.grid()
        self.buttn1.configure(bg="pink")
        self.label = Label(self, text="this is a button")
        self.label.grid()

        #2nd button
        self.buttn2 = Button(self)
        self.buttn2.grid()
        self.buttn2.configure(text="button 2", bg="pink")
        self.label = Label(self,text="this is a button")
        self.label.grid()

        #3rd button
        self.buttn3 = Button(self)
        self.buttn3.grid()
        self.buttn3["text"] = "button 3"
        self.buttn3["bg"] = "yellow"
        self.buttn3["fg"] = "purple"


root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()