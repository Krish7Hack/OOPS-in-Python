class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def show(self):
        print("Hello from Child")

#Instaniate Child Class
child=Child() #object of child class
child.greet() #calling parent class method
child.show() #calling child class method
