import math
class Point():
    def __init__ (self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(f"coordinates: ({self.x}, {self.y})")
    def move(self, x2, y2):
        self.x=x2
        self.y=y2
    def dist(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance


point1 = Point(int(input()), int(input()))
point1.show()
point1.move(int(input()), int(input()))
point2 = Point(int(input()), int(input()))

point1.show()
point2.show()
distance = point1.dist(point2)
print(distance)
