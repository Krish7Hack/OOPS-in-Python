#Multiple Inheritance -> Parent and Son functions in GrandSon
class Parent:
    def greet1(self):
        print("Hello from Parent")

class Son:
    def greet2(self):
        print("Hello from Son")

class GrandSon(Parent, Son):
    def greet(self):
        print("Hello from GrandSon")

grandSon=GrandSon()
grandSon.greet1()
grandSon.greet2()
grandSon.greet()