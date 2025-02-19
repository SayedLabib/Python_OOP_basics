
class person(object):

    def __init__(self, name):
        
        self.name = name

    def speak(self):
        print("Hi I am " + self.name)

Fuad = person('SayedLabib')
Fuad.speak()


class Animal(object):

    def __init__(self, dog, cat, bird):
        self.dog = dog
        self.cat = cat
        self.bird = bird

    def dog_habit(self):
       print(self.dog+"Gurd the owner")
   
    def cat_habit(self):
        print(self.cat+"Doesn't care about the owner")

    def bird_habit(self):
        print(self.bird+"Likes the company of the owner")    

animal = Animal('PitBull','Parsian','Cokatail')

animal.dog_habit()

animal.cat_habit()

animal.bird_habit()
