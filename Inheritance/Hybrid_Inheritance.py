#Hybrid Base->mix of hierarchical and multiple inheritance
class Base:
    def greet_base(self):
        print("Hello from base")

class Parent1(Base):
    def greet_parent1(self):
        print("Hello from parent1")

class Parent2(Base):
    def greet_parent2(self):
        print("Hello from parent2")

class Child(Parent1,Parent2):
    def greet_child(self):
        print("Hello from child")

child=Child()
child.greet_base()
child.greet_parent1()
child.greet_parent2()
child.greet_child()