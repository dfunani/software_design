# Head First: Design Patterns

## Object Oriented Programming Principles

### 1. Abstraction

**Definition**: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object.

```python
class Car:
    def start(self):
        print("Started!")

    def stop(self):
        print("Stopped!")

    def __reset_pistons__(self):
        print("Abstraction of how Pistons work.")
```

### 2. Encapsulation

**Definition**: Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit, typically a class, and restricting access to some of the object's components.

```python
class Car:
    def start(self):
        print("Started!")

    def stop(self):
        print("Stopped!")

    def speedometer(self):
        print("My Speed Is, 120KM/H!")
```

### 3. Polymorphism

**Definition**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It provides a way to use a single interface to represent different underlying forms (data types).

```python
from abc import ABC, abstractmethod

class ICar(ABC):
    @abstractmethod
    def display(self):
        pass

class Audi(ICar):
    def display(self):
        print("This is an Audi!")

class BMW(ICar):
    def display(self):
        print("This is a BMW!")

bmw = BMW()
bmw.display()  # Output: This is a BMW!

audi = Audi()
audi.display()  # Output: This is an Audi!
```

### 4. Inheritance

**Definition**: Inheritance is the mechanism by which one class (child or subclass) inherits the attributes and methods from another class (parent or superclass).

```python
class Vehicle:
    def speedometer(self):
        print("My Speed Right Now!")

class Audi(Vehicle):
    def drive(self):
        print("Vroom Vroom")

audi = Audi()
audi.speedometer()  # Output: My Speed Right Now!
audi.drive()        # Output: Vroom Vroom
```

## Design Principles

1. Separate things that change or vary from those that stay the same.
2. Program to an Interface, not an Implementation.
3. Favour Composition over Inheritance.

## Design Patterns

### 1. Strategy Pattern - Payment Processing System

**Example**: Payment Processing System. This system can support multiple payment methods such as *credit card*, *PayPal*, and *cryptocurrency*. Each payment method is a strategy that can be selected at runtime.