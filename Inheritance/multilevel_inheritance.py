#Multilevel Inheritance -> Stepwise Inheritance from one class to another
class GrandParent:
    def greet_grandparent(self):
        print("Hello, I am GrandParent")

class Parent(GrandParent):
    def greet_parent(self):
        print("Hello, I am Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello, I am Child")

child=Child()
child.greet_grandparent()
child.greet_parent()
child.greet_child()