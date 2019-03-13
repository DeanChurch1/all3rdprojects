#Dean Church
#calculator

from tkinter import*

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.add()
        self.subtract()
        self.multiply()
        self.divide()
        self.calculator()
        self.clear_screen()
        self.insert_screen()

    def create_widgets(self):
        Label(self, text = "Calculator").grid(row = 0, column = 0, sticky = W)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD).grid(row = 0, column = 1,columnspan = 4, sticky = W)

        self.bttn1 = Button(self, text = "1",width = 7,command = self.bttn1_press).grid(row = 2, column = 1, sticky = W)
        self.bttn2 = Button(self, text = "2",width = 7,command = self.bttn2_press).grid(row = 2, column = 2, sticky = W)
        self.bttn3 = Button(self, text = "3",width = 7,command = self.bttn3_press).grid(row = 2, column = 3, sticky = W)
        self.bttn4 = Button(self, text = "4",width = 7,command = self.bttn4_press).grid(row = 3, column = 1, sticky = W)
        self.bttn5 = Button(self, text = "5",width = 7,command = self.bttn5_press).grid(row = 3, column = 2, sticky = W)
        self.bttn6 = Button(self, text = "6",width = 7,command = self.bttn6_press).grid(row = 3, column = 3, sticky = W)
        self.bttn7 = Button(self, text = "7",width = 7,command = self.bttn7_press).grid(row = 4, column = 1, sticky = W)
        self.bttn8 = Button(self, text = "8",width = 7,command = self.bttn8_press).grid(row = 4, column = 2, sticky = W)
        self.bttn9 = Button(self, text = "9",width = 7,command = self.bttn9_press).grid(row = 4, column = 3, sticky = W)
        self.bttn0 = Button(self, text = "0",width = 7,command = self.bttn0_press).grid(row = 5, column = 2, sticky = W)
        self.bttn10 = Button(self, text = "+",width = 7,command = self.bttn10_press).grid(row = 2, column = 4, sticky = W)
        self.bttn11 = Button(self, text = "-",width = 7,command = self.bttn11_press).grid(row = 3, column = 4, sticky = W)
        self.bttn12 = Button(self, text = "*",width = 7,command = self.bttn12_press).grid(row = 4, column = 4, sticky = W)
        self.bttn13 = Button(self, text = "/",width = 7,command = self.bttn13_press).grid(row = 5, column = 4, sticky = W)
        self.bttn14 = Button(self, text = "=",width = 7,command = self.bttn14_press).grid(row = 6, column = 4, sticky = W)
        

    def btt1_press(self):
        self.displayarea += 1
        

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass




    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        self.equation += str(value)
        self.screen.configure(state ='disabled')




root = Tk()
root.title("Calculator")
root.geometry("500x500")
app = Application(root)
root.mainloop()
