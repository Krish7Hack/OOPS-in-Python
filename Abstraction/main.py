from shapes import Rectangle

rect = Rectangle(10,5)

#Accessing attributes via public methods
print("Length:",rect.get_length())
print("Area:",rect.area())
print("Periemeter:",rect.perimeter())

#Updated length using setter
rect.set_length(15)

print("Updated Length:",rect.get_length())
print("Updated Area:",rect.area())