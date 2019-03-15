#Dean Church
#Madlib

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        tkinter.Label(self, text="MADLIB").grid(row=0, column=0, columnspan=3, sticky=tkinter.W)

        # Name
        tkinter.Label(self,text = "Country 1: ").grid(row = 1, column = 0, sticky = tkinter.W)
        self.country1_ent = tkinter.Entry(self)
        self.country1_ent.grid(row = 1, column = 1, sticky = tkinter.W)

        # Second name
        tkinter.Label(self,
              text = "Country 2: ").grid(row = 2, column = 0, sticky = tkinter.W)
        self.country2_ent = tkinter.Entry(self)
        self.country2_ent.grid(row = 2, column = 1, sticky = tkinter.W)

        # Year
        tkinter.Label(self,
              text = "Year: ").grid(row = 3, column = 0, sticky = tkinter.W)
        self.year_ent = tkinter.Entry(self)
        self.year_ent.grid(row = 3, column = 1, sticky = tkinter.W)

        # Integer
        tkinter.Label(self, text="Integer:").grid(row=4, column=0, sticky=tkinter.W)
        self.integer_ent = tkinter.Entry(self)
        self.integer_ent.grid(row=4, column=1, sticky = tkinter.W)

        # Average
        tkinter.Label(self,
              text = "Number:"
              ).grid(row = 5, column = 0, sticky = tkinter.W)

        self.average = tkinter.StringVar()
        self.average.set(None)

        averages = ["0.124", "0.315", "0.762"]
        column = 1
        for average in averages:
            tkinter.Radiobutton(self,
                        text = average,
                        variable = self.average,
                        value = average).grid(row = 5, column = column, sticky = tkinter.W)
            column += 1

        # Adjectives
        tkinter.Label(self, text="Player 2 was: ")
        self.loony = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Loony",
                    variable = self.loony
                    ).grid(row = 6, column = 1, sticky = tkinter.W)

        self.crazy = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Crazy",
                    variable = self.crazy
                    ).grid(row = 6, column = 2, sticky = tkinter.W)

        self.weird = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Weird",
                    variable = self.weird
                    ).grid(row = 6, column = 3, sticky = tkinter.W)


        # Tell Story
        tkinter.Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 7, column = 0, sticky = tkinter.W)

        self.story_txt = tkinter.Text(self, width = 75, height = 10, wrap = tkinter.WORD)
        self.story_txt.grid(row = 8, column = 0, columnspan = 4)

    def tell_story(self):
        year = self.year_ent.get()
        player1 = self.country1_ent.get()
        player2 = self.country2_ent.get()
        integer = self.integer_ent.get()
        average = self.average.get()
        p1hr = 36
        p2hr = p1hr + int(integer);

        adj = ""
        if self.loony.get():
            adj += ", loony"
        if self.weird.get():
            adj += ", weird"
        if self.crazy.get():
            adj += ", crazy"


        story += "It was "
        story += year
        story += ", the world is in chaos and is in the middle of the apocalypse. It was between the countries "
        story += country1
        story += " and "
        story += country2
        story += ". "
        story += country1 + " was selfish" + adj + ", and big. "
        story += country2 + " was powerhungry and would do anything to win. "
        story += "However, both countries had powerful and destructive weapons. "
        story += country1 + " was bent on world domination and " + country2 + " would destroy any country that opposed them. "
        story += "That year, " + country1 + " had the wider global reach with " + average + "countries under their control. "
        story += "However, "+ country2 + " had " + integer + " more powerful weapons with a larger military " + str(p1hr) +", while " + country1 + " had " + str(p2hr) + ". "
        story += "Unfortunetly, the world could not conclude who was the best country was, " + player1 + " or " + player2 + ", both destroyed themselves by accidently dropping nukes on their own headquarters."

        self.story_txt.delete(0.0, tkinter.END)
        self.story_txt.insert(0.0, story)


root = tkinter.Tk()
root.title("mad lib")
app = Application(root)
root.mainloop()

