class Shape:
    def area(self,a,b=None):
        if b is None: #Overloading
            return a*a
        else:
            return a*b
        
class Circle(Shape):
    def area(self,radius,b=None): #Overriding
        return 3.14 * radius * radius
    
square=Shape()
rectangle=Shape()
circle=Circle()

print(square.area(5))
print(rectangle.area(4,5))
print(circle.area(5))
