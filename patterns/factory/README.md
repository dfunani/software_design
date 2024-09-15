# Decorator Pattern

## Definition:

The Factory Pattern is often used to encapsulate the complexity of creating objects, making the code more flexible and easier to maintain. Can be implemented as a Simple Factory, a Factory Method or a Abstract Factory.

1. Simple Factory: A simple factory is a class that creates objects of related types based on a parameter.

```python
from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from enum import Enum

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Shapes(Enum):
    CIRCLE = Circle
    RECTANGLE = Rectangle

class ShapeFactory():
    def getShape(self, shape: Shapes) -> Shape:
        if not isinstance(shape, Shapes):
            raise ShapeException()
        return shape.value()

class Canvas:
    def __init__(self, factory: ShapeFactory):
        self.factory = factory

    def paint(self, shape: Shapes):
        self.factory.getShape(shape).draw()

factory = ShapeFactory()
canvas = Canvas(factory)
canvas.paint(Shapes.RECTANGLE)
canvas.paint(Shapes.CIRCLE)
```

2. Factory Method: A factory method defines an interface for creating an object, but lets subclasses decide which class to instantiate.

```python
from abc import ABC, abstractmethod
from enum import Enum

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Canvas(ABC):
    @abstractmethod
    def get_shape(self):
        pass
        
    def paint(self):
        self.get_shape().draw()

class CircleCanvas(Canvas):
    def get_shape(self) -> Shape:
        return Circle()
    
class RectangleCanvas(Canvas):
    def get_shape(self) -> Shape:
        return Rectangle()

# Circle Canvas
canvas = CircleCanvas()
canvas.paint()

# Rectangle Canvas
canvas = RectangleCanvas()
canvas.paint()
```

3. Abstract Factory: An abstract factory provides an interface for creating families of related or dependent objects without specifying their concrete classes.

```python
from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from enum import Enum

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class BorderedCircle(Shape):
    def draw(self):
        print("Drawing a circle - Bordered")

class BorderedRectangle(Shape):
    def draw(self):
        print("Drawing a rectangle - Bordered")

class ShapeFactory(ABC):
    @abstractmethod
    def create_circle(self) -> Shape:
        pass
    @abstractmethod
    def create_rectangle(self) -> Shape:
        pass

class StandardShapeFactory(ShapeFactory):
    def create_circle(self):
        return Circle()
    
    def create_rectangle(self):
        return Rectangle()
    
class BorderedShapeFactory(ShapeFactory):
    def create_circle(self):
        return BorderedCircle()
    
    def create_rectangle(self):
        return BorderedRectangle()

class Canvas(ABC):
    def __init__(self, factory: ShapeFactory) -> None:
        self.factory = factory

    def paint(self):
        self.factory.create_circle().draw()
        self.factory.create_rectangle().draw()

# Draws a Shape
canvas = Canvas(StandardShapeFactory())
canvas.paint()

# Draws a Bordered Shape
canvas = Canvas(BorderedShapeFactory())
canvas.paint()
```

## Use Case:

Simple Factory: Suitable for small-scale applications or when the creation logic is straightforward.
Factory Method: Ideal when you need to decouple the creation of objects from the client code and allow subclasses to customize the creation process.
Abstract Factory: Appropriate for creating families of related objects that are consistent with each other, especially in large-scale applications.

## Summary:

Factory patterns are design patterns that provide a way to create objects without exposing their creation logic. They encapsulate the complexity of object creation, making the code more flexible and easier to maintain.