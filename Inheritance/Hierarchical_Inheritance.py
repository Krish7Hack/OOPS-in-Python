#Hierarchical Inheritance -> Multiple child classes inherit from a single parent class
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def show1(self):
        print("Hello from Child1")

class Child2(Parent):
    def show2(self):
        print("Hello from Child2")

child1 = Child1()
child2 = Child2()

child1.greet()
child1.show1()

child2.greet()
child2.show2()