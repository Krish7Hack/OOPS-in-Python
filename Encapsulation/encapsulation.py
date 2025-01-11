#Encapsulation in python
class Person:
    def __init__(self,name,age):
        self.name=name
        self._address ="Unknown" #Protected attribute->can only be used where it is defined or its subclass
        self.__age=age #Private attribute->can only be accessed within the class itself

    #Public method to access private attribute
    def get_age(self):
        return self.__age
    
    #Public method to  update private attribute
    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age")

    #Public method to display details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")#Use of getters for accessing private attributes
        print(f"Address: {self._address}")

person=Person("Krishna",30) #Creating an object of the class.

print("Name:",person.name) #Accessing public attribute

print("Address:",person._address) #Accessing protected attribute

#print(person.__age)#Accessing private attribute

#Using public method to access private attribute
print("Age (using getter)",person.get_age())
#Using public method to update private attribute
person.set_age(31)
print("Age (using setter)",person.get_age())

person.display_details()