#Polyniorphism->same name but perform distinct tasks
class Shape:
    def area(self):
        return "Undefined"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
shapes=[Rectangle(2,3),Circle(5)]
for shape in shapes:
    print("Area:",shape.area())