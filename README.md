# OOPS-in-Python
# Object-Oriented Programming (OOP) Basics

This repository demonstrates the fundamental principles of Object-Oriented Programming (OOP) using Python. The four key principles of OOP are:

1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**
4. **Abstraction**

Each principle is explained with code examples for better understanding.

---

## Principles and Examples

### 1. Encapsulation

Encapsulation is the process of bundling data and the methods that operate on that data within a single unit (class). It also involves restricting direct access to some properties using private attributes (indicated by a leading underscore or double underscore).

**Example:**

```python
class BankAccount:
    def __init__(self, account_holder_name, initial_balance):
        self.__account_holder_name = account_holder_name
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

# Usage
if __name__ == "__main__":
    account = BankAccount("Alice", 1000.0)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance: ${account.get_balance()}")

### 2. Inheritance

Inheritance allows one class (child) to inherit properties and methods from another class (parent). It promotes code reuse and establishes a relationship between classes.

### Example:

```python
class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

# Usage
if __name__ == "__main__":
    dog = Dog()
    dog.eat()  # Inherited method
    dog.bark()  # Dog's own method

## 3. Polymorphism

### 1. Method Overloading

Python does not support method overloading directly, but we can achieve similar functionality using **default arguments**.

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Usage
if __name__ == "__main__":
    calc = Calculator()
    print("Sum of two numbers:", calc.add(5, 10))      # Output: 15
    print("Sum of three numbers:", calc.add(5, 10, 15))  # Output: 30
2. Method Overriding
In method overriding, a method in a child class has the same name as a method in the parent class but provides a different implementation.

python
Copy code
class Shape:
    def draw(self):
        print("Drawing a shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

# Usage
if __name__ == "__main__":
    shape = Circle()
    shape.draw()  # Output: Drawing a circle

## 4. Abstraction

### 1. Abstract Base Class

An **Abstract Base Class (ABC)** is a class that cannot be instantiated and serves as a blueprint for other classes. Abstract methods defined in an ABC must be implemented in derived classes.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button.")

# Usage
if __name__ == "__main__":
    car = Car()
    car.start()  # Output: Car starts with a key.

    bike = Bike()
    bike.start()  # Output: Bike starts with a button.
