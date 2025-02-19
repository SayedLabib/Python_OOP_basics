
# Overriding concepts

class Point() :
    def __init__(self,x=0, y=0):

        self.x = x
        self.y = y
        self.coord = (self.x,self.y)

    def change(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):

        return Point(self.x + p.x, self.y + p.y)

    def __str__(self):
       return f"Point {self.x}, {self.y}"


p1 = Point(4,10)

p2 = Point(5,13)

p3 = p1 + p2  # Overriding add method 

p4 = Point(5,14)

p4.change(2, 3) # Overriding change method

print(p3)
