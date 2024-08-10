# Observer Pattern

## Definition:

The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

### Newspaper Publisher - Subject

We define a NewspaperSubject that will publish newspapers to any subscribers.

```python
from abc import ABC, abstractmethod

class ISubject(ABC):
    @abstractmethod
    def register_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class NewspaperSubject(ISubject):
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer: IObserver):
        self.__observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.__observers.remove(observer)

    def notify_observers(self):   
        for observer in self.__observers:
            observer.update(self)   
```

### Newspaper Subscribers - Observers

We define Subscribers such as *business*, *people*, *hotels*, *airlines*, and *other businesses*. All registered subscribers will have a "Newspaper" delivered to them.

```python
class IObserver(ABC):
    def __init__(self, subject: "ISubject") -> None:
        # Register observers with the publisher
        subject.register_observer(self)

    @abstractmethod
    def update(self, subject: ISubject):
        pass

class BusinessObserver(IObserver):
    def update(self, subject: ISubject):
        # Business logic for handling newspaper updates
        print("Business received the newspaper.")

class PeopleObserver(IObserver):
    def update(self, subject: ISubject):
        # People logic for handling newspaper updates
        print("People received the newspaper.")

class HotelObserver(IObserver):
    def update(self, subject: ISubject):
        # Hotel logic for handling newspaper updates
        print("Hotel received the newspaper.")

class AirlineObserver(IObserver):
    def update(self, subject: ISubject):
        # Airline logic for handling newspaper updates
        print("Airline received the newspaper.")

class OtherBusinessesObserver(IObserver):
    def update(self, subject: ISubject):
        # Other businesses logic for handling newspaper updates
        print("Other businesses received the newspaper.")

# Create a newspaper publisher
newspaper_publisher = NewspaperSubject()

# Create observers
business_observer = BusinessObserver(newspaper_publisher)
people_observer = PeopleObserver(newspaper_publisher)

# Simulate a new newspaper publication
newspaper_publisher.notify_observers()
```

## Use Case:

The Observer Pattern is valuable in systems where objects need to be notified and updated automatically when the state of another object changes. It decouples the subject (the object being observed) from its dependents (observers), promoting flexibility and maintainability. This pattern is essential for building systems that require real-time updates or event-driven architectures.

## Summary:

The Observer pattern effectively decouples the newspaper publisher (subject) from its subscribers (observers). The publisher maintains a list of subscribers and notifies them when a new newspaper is available. Subscribers implement their specific update logic based on the received update information.
````

