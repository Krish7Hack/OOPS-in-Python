#Single Inheritance
class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car start...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):

    def __init__(self,name):
        self.name = name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Prius")

print(car1.name)
print(car1.start())
print(car1.color)

#Multi-Level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car start...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):

    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1=Fortuner("Diesel")
print(car1.start())

#Multiple Inheritance
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"

class C(A,B):
    varC="Welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super Method
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car start...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):

    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1=ToyotaCar("Prius","electric")
print(car1.type)

#Class Method
class Person:

    name="Krishna"

    # def changeName(Self,name):
    #     Self.name=name
    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Kriti")
print(p1.name)
print(Person.name)

#Property Method
class Student:
    def __init__(self, phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        

    # def clacPercentage(self):
    #     self.percentage=str((self.phy + self.chem + self.math) / 3)+ "%"
    @property
    def clacPercentage(self):
        return str((self.phy + self.chem + self.math) / 3)+ "%"

stu1=Student(98,97,99)
print(stu1.clacPercentage)

stu1.phy=86
print(stu1.clacPercentage)