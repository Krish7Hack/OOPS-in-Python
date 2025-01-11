#Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class.
class Parent:
    def greet(self):
        print("Hello, I am a parent")

class Child(Parent):
    def greet(self):
        print("Hello, I am a child")

parent=Parent()
child=Child()

print(parent.greet())
print(child.greet()) #Calls the overridden method form Child