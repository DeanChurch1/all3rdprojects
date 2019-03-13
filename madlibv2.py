#Dean Church
#Madlib

from tkinter import*

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        Label(self,text = "New Story").grid(row = 0, column = 0, sticky = W)
        #row 2
        Label(self,text = "Person").grid(row = 1, column = 0, sticky = W)
        #row 3
        Label(self,text = "Plural Noun").grid(row = 2, column = 0, sticky = W)
        #row 4
        Label(self,text = "Verb").grid(row = 3, column = 0, sticky = W)
        #row 5
        Label(self,text = "Adjective").grid(row = 4, column = 0, sticky = W)
        Checkbutton(self, text = "Itchy").grid(row = 4,column = 1, sticky = W)
        
        Checkbutton(root, text = "Joyous").grid(row = 4,column = 2, sticky = W)
        
        Checkbutton(root, text = "electric").grid(row = 4,column = 3, sticky = W)

        #row 6
        Label(self,text = "Body part:").grid(row = 5, column = 0, sticky = W)
        Radiobutton(self,
                    text = "Finger",
                    value = "finger"
                    ).grid(row = 5 , column = 2, sticky = W)
        Radiobutton(self,
                    text = "Arm",
                    value = "arm"
                    ).grid(row = 5, column = 3, sticky = W)
        Radiobutton(self,
                    text = "Hand",
                    value = "hand"
                    ).grid(row = 5, column = 4, sticky = W)

        #row 7
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Submit"

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy,"
        if self.is_joyous.get():
            adjectives += "electric,"
        if self.is_electric.get():
            adjectives += "electric,"
        #body_part




        self.story_txt.delete(0.0,END)
        self.stroy_txt.insert(0.0,story)

root = Tk()
root.title("MadLib")
root.geometry("300x150")
app = Application(root)
root.mainloop()
