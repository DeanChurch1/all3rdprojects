#Dean Church
#Tamagachi

def Human(object):

    def __init__( self,name,hair_color,eye_color,height,weight,iq,gender,race):
        name = name
        hair_color = hair_color
        eye_color = eye_color
        height = height
        weight = weight
        iq = iq
        gender = gender
        race = race
    def introduce_self(self):
        print("hello my name is ",self.name)
    def discribe_self(self):
        print("I have ", self.color_hair, "hair")
        print("I have ", self.eye_color, "eyes")
        print("I am ", self.height, "tall")
        print("I weigh ", self.weight, "lbs")
        print("I have ", self.iq, "iq")
        print("I am ", self.race, "race", self.gender, "gender", "I have a", self.iq, "iq")

eric = Human("eric","blue","green",1000,2490,23,"na","purple")
eric.introduce_self()
eric.discribe_self()
