#Dean Church
#Tamagachi

class Human(object):

    def __init__(self,name,hair_color,eye_color,height,weight,iq,gender,race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def introduce_self(self):
        print("\nhello my name is",self.name)
    def discribe_self(self):
        print("I have "+self.hair_color+" hair")
        print("I have "+self.eye_color+" eyes")
        print("I am",self.height,"feet tall")
        print("I weigh ",self.weight," lbs")
        print("I am "+self.race+" race.","I am a "+ self.gender+" gender."," I have a",self.iq,"iq")
    def bmi_test(self):
        height2 = self.height*self.height
        weight2 = 703*self.weight
        bmi_division = weight2/height2
        print(bmi_division)
        if bmi_division <= 18.5:
            print(self.name,"is underweight")
        elif bmi_division >= 18.5 and bmi_division <= 24.9:
            print(self.name,"is normal")
        elif bmi_division >= 25 and bmi_division <= 29.9:
            print(self.name,"You are overweight")
        else:
            print(self.name,"You are obese")



Eric = Human("eric","blue","green",72,160,23,"na","purple")
Eric.introduce_self()
Eric.discribe_self()
Eric.bmi_test()

Jake = Human("Jake","yellow","pink",90,700,4,"boat","indian")
Jake.introduce_self()
Jake.discribe_self()

Quentin = Human("Quentin","blue","brown",6,250,79,"Male","Chinese")
Quentin.introduce_self()
Quentin.discribe_self()

class Critter(object):

