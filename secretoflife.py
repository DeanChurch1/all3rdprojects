from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create button, text, and entry widgets."""
        self.inst_lbl = Label(self, text = "Enter password for the secret of life")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #create label
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        #create entry widget
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        #create submit button
        self.submit_bttn = Button(self, text = "submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        #create text widget
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        pass










#Main
root = Tk()
root.title("secret of life")
root.geometry("300x150")

app = Application(root)

root.mainloop()
