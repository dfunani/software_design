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
4. Strive for loosely coupled designs for objects that interact.
5. Classes should be open for extension, but closed for modification.
6. Dependency Inversion Principle: Depend upon abstractions. Not upon concrete implementations.

## Design Patterns

### 1. Strategy Pattern - Payment Processing System

**Example**: Payment Processing System. This system can support multiple payment methods such as _credit card_, _PayPal_, and _cryptocurrency_. Each payment method is a strategy that can be selected at runtime.

### 2. Observer Pattern - Weather Monitoring System

**Example**: Weather Monitoring System. This system supports notifying multiple weather displays, such as _Current Conditions_, _Weather Statistics_, and _Simple Forecasts_, of any change in weather conditions. Each weather display subscribes to a Central Weather Data Object, which is then responsible for pushing data to the displays at runtime.

### 3. Decorator Pattern - Coffee Shop

Example: A coffee shop can offer a variety of coffee drinks, such as _Espresso_, _Latte_, and _Cappuccino_. Additional **toppings** and **flavors**, like _milk_, _sugar_, and _syrup_, can be added dynamically to create different variations of coffee. The Decorator pattern allows you to combine base coffee drinks with various toppings and flavors to create customized products.

### 4. Factory Pattern - Pizza Shop

Example: A Pizza Shop offers various types of pizzas, such as _Pepperoni_, _Margherita_, and _Hawaiian_. Each pizza has its own specific ingredients and preparation method. The Factory Pattern provides a way to create different pizza objects without exposing their creation logic.

### 5. Singleton Pattern - Logging System

In a logging system, it's often desirable to have only one instance of a logger class to ensure consistent logging behavior across the application. The Singleton Pattern guarantees that there's only one instance of the logger, preventing potential conflicts and ensuring that all log messages are handled in the same way.

### 6. Command Pattern - Home Automation System

In a home automation system, users interact with various devices (e.g., lights, thermostats and TVs) through different interfaces (e.g., mobile app, voice control). Managing these interactions can become complex and error-prone. The Command Pattern decouples the object that invokes a request (the invoker) from the one that knows how to perform it (the receiver).

### 7. Adapter Pattern - Home Automation System

In a home automation system, devices often have incompatible interfaces. The Adapter Pattern allows these devices to work together by translating requests from the system into commands understood by the specific device. This promotes flexibility and reusability, enabling the system to integrate various devices without modifying their core functionality.
