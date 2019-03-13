from tkinter import*


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Total Clicks: 0"
        self.bttn1["command"] = self.update_count
        self.bttn1.grid()

    def update_count(self):
        """Increase click count and display new total."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

    def negative_count(self):
        self.bttn_clicks -= 1
        self.bttn["text"] = "Total clicks: " + str(self.bttn_clicks)







root = Tk()
root.title("Click counter")
root.geometry("200x50")
app = Application(root)
root.mainloop()