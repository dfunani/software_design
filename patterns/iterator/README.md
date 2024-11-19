# Iterator Pattern

## Definition

The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

### Menus

    ```python
    from abc import ABC, abstractmethod

    class Menu(ABC):
        @abstractmethod
        def create_iterator(self):
            pass

    class BreakfastMenu(Menu):
        def __init__(self):
            self.items = ["Pancakes", "Omelette", "Toast"]

        def create_iterator(self):
            return BreakfastIterator(self)

    class LunchMenu(Menu):
        def __init__(self):
            self.items = ["Burger", "Pizza", "Salad"]

        def create_iterator(self):
            return LunchIterator(self)

    class DinnerMenu(Menu):
        def __init__(self):
            self.items = ["Steak", "Pasta", "Seafood"]

        def create_iterator(self):
            return DinnerIterator(self)
    ```
    
### Iterators

    ```python
    class Iterator(ABC):
        @abstractmethod
        def has_next(self):
            pass

        @abstractmethod
        def next(self):
            pass

    class BreakfastIterator(Iterator):
        def __init__(self, menu):
            self.menu = menu
            self.position = 0

        def has_next(self):
            if self.position >= len(self.menu.items):
                return False
            return True

        def next(self):
            item = self.menu.items[self.position]
            self.position += 1
            return item

    class LunchIterator(Iterator):
        def __init__(self, menu):
            self.menu = menu
            self.position = 0

        def has_next(self):
            if self.position >= len(self.menu.items):
                return False
            return True

        def next(self):
            item = self.menu.items[self.position]
            self.position += 1
            return item

    class DinnerIterator(Iterator):
        def __init__(self, menu):
            self.menu = menu
            self.position = 0

        def has_next(self):
            if self.position >= len(self.menu.items):
                return False
            return True

        def next(self):
            item = self.menu.items[self.position]
            self.position += 1
            return item
    ```

### Menu Render

    ```python

    # Usage:
    breakfast_menu = BreakfastMenu()
    breakfast_iterator = breakfast_menu.create_iterator()

    print("Breakfast Menu:")
    while breakfast_iterator.has_next():
        item = breakfast_iterator.next()
        print(item)

    lunch_menu = LunchMenu()
    lunch_iterator = lunch_menu.create_iterator()

    print("\nLunch Menu:")
    while lunch_iterator.has_next():
        item = lunch_iterator.next()
        print(item)

    dinner_menu = DinnerMenu()
    dinner_iterator = dinner_menu.create_iterator()

    print("\nDinner Menu:")
    while dinner_iterator.has_next():
        item = dinner_iterator.next()
        print(item)

    ```

## Benefits

1. Decoupling:

- Separates the collection from the iteration logic, making the code more modular and easier to understand.
- Reduces coupling between the collection and the client code.

2. Flexibility:

- Allows different iteration algorithms for different data structures.
- Supports various traversal strategies (e.g., forward, backward, random access).

3. Reusability:

- The iterator pattern can be applied to various data structures, making it a versatile design pattern.

4. Simplified Client Code:

- Clients can iterate over different collections using a consistent interface, simplifying the code.

5. Encapsulation:

- Hides the internal structure of the collection from the client.
- Protects the collection from modification during iteration.

6. Efficient Iteration:

- Can optimize iteration for specific data structures (e.g., linked lists, arrays).

## Use Case

The Iterator Pattern is a versatile design pattern with numerous applications in software development. Here are some common use cases:

1. Iterating Over Collections:

- Arrays: Iterating over elements of an array.
- Linked Lists: Traversing nodes in a linked list.
- Trees: Traversing nodes in a tree structure (e.g., depth-first search, breadth-first search).

2. File System Iteration:

- Iterating over files and directories in a file system.

3. Database Query Results:

- Iterating over rows in a database query result set.

4. GUI Component Iteration:

- Iterating over child components of a container in a GUI framework.

5. Network Protocol Parsing:

- Iterating over packets in a network protocol.

6. XML/JSON Parsing:

- Iterating over elements and attributes in XML or JSON documents.

7. Custom Data Structures:

- Iterating over elements in custom data structures like stacks, queues, or graphs.

## Summary

The Iterator Pattern provides a powerful and flexible way to access and traverse elements in a collection without exposing its underlying implementation details. It promotes code clarity, maintainability, and reusability.
