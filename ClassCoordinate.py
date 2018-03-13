from math import sqrt

class Coordinate:
    
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y **2)
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    def __str__(self):
        return "X = " + str(self.x) + ",Y = " + str(self.y)
    
    def get (self):
        return self.x
    
    
        

p1 = Coordinate(3, 4)
p2 = Coordinate(3, 4)
print(p1.x, p1.y)
print(p1.magnitude())
#p1.translate(1, 1)
print(p1.x, p1.y)
print(p1 == p2)
print(p1)
print(p1.get())