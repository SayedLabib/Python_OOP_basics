class Animal(object):
    def __init__(self, color,coat):

      self.color = color
      self.coat = coat
     

class Dog(Animal):

    def __init__(self,color, coat,eat):
       super().__init__(color,coat)
       self.eat = eat
       
    def behaviors(self):
      print(f"{self.color} Colored Dog have {self.coat} coat and eats {self.eat}")   

class Cat(Animal):
   
   def __init__(self,color,coat, eat):
       super().__init__(color,coat)
       self.eat = eat
       
   def behaviors(self):
      print(f"{self.color} Colored Cat have {self.coat} coat and eats {self.eat}")



dog = Dog('Brown', 'Short', 'Meat')
cat = Cat('White', 'Fluffy', 'Cat food')

dog.behaviors()
cat.behaviors()

         