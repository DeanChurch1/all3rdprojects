from tkinter import*


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Positive clicker"
        self.bttn1["command"] = self.update_count
        self.bttn1.grid()
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Negative clicker"
        self.bttn2["command"] = self.negative_count
        self.bttn2.grid()
        self.label = Label(self, text="Total clicks: " + str(self.bttn_clicks))
        self.label.grid()

    def update_count(self):
        """Increase click count and display new total."""
        self.bttn_clicks += 1
        self.bttn1["text"] = "positive clicker " + str(self.bttn_clicks)       
        self.label = Label(self, text="Total clicks: " + str(self.bttn_clicks))
        self.label.grid()
            
        
    def negative_count(self):
        self.bttn_clicks -= 1
        self.bttn2["text"] = "Negative clicker " + str(self.bttn_clicks)
        self.label = Label(self, text="Total clicks: " + str(self.bttn_clicks))
        self.label.grid()






root = Tk()
root.title("Click counter")
root.geometry("400x400")
app = Application(root)
root.mainloop()
