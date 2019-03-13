#Dean Church
#critter

class Critter(object):

    def __init__(self,name,hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom


    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1


    def play(self,fun = 4):
        print("You are playing with",self.name)
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def talk(self):
        print("This is",self.name,"They feel",self.mood)
        self.__pass_time()

    def eat(self,food = 4):
        print("Your critter's hunger is",self.hunger)
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        print("Your critter's current happiness is",unhappiness)
        if unhappiness < 5:
            m = "happy"
        elif unhappiness >= 5 and unhappiness <= 10:
            m = "okay"
        elif unhappiness >= 11 and unhappiness <= 14:
            m = "frustrated"
        else:
            print("Your critter has died")
        return m

def main():
    crit_name = input("What do you want to name your Critter: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        choice = input("Would you like to\n1:Play with your critter\n2:Talk to your critter\n3:Feed your critter\n")
        if choice == "0":
            print("good bye")
        elif choice == '1':
            crit.play()
        elif choice == '2':
            crit.talk()
        elif choice == '3':
            crit.eat()
        else:
            print("Not a good choice")


main()
