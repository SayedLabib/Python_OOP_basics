
# Static method and class method

class Dog():
    dogs = []

    def __init__(self,name):
     self.name = name
     self.dogs.append(self)


    @classmethod
    def num_dogs(cls):
       return len(cls.dogs)
    
    @staticmethod

    def dogs_bark(n):
       
       for __ in range(n):
          print("barking dog !!")

Shepard = Dog("German Shepard")
pitBull = Dog("PitBull")

Dog.dogs_bark(5)