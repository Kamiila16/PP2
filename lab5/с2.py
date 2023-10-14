class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__ (self, length):
        self.length = length
    def area(self):
        return self.length**2
    
shape = Shape()
square = Square(int(input()))


print("Area of the generic shape:", shape.area())
print("Area of the square:", square.area())



