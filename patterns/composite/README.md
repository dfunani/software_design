# Composite Pattern

## Definition

The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

### Component

```python
from abc import ABC, abstractmethod
from typing import Iterator, List


class Node(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Component(Node):
    def __init__(self):
        self.children: List[Node] = []

    def add_child(self, child: Node):
        self.children.append(child)

    def get_name(self):
        # Get names from children recursively
        for child in self.children:
            child.get_name()

    def execute(self):
        # Execute actions of children recursively
        for child in self.children:
            child.execute()

    def __iter__(self) -> Iterator[Node]:
        return iter(self.children)

class Button(Node):
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def execute(self):
        print(f"Button {self.text} clicked!")

    def get_name(self):
        print(f"Button: {self.name}")


class TextBox(Node):
    def __init__(self, name, placeholder):
        self.name = name
        self.placeholder = placeholder

    def execute(self):
        print(f"Text Box {self.placeholder} activated!")

    def get_name(self):
        print(f"Text Box: {self.name}")
```

### Usage

```python
# Usage:
window = Window()

button = Button("Button 1", "Click me")
textBox = TextBox("Text Box 1", "Enter text")

button1 = Button("Button 2", "Click me")
textBox1 = TextBox("Text Box 2", "Enter text")
panel = Component()

panel.add_child(button)
panel.add_child(textBox)

window.add_child(panel)
window.add_child(button1)
window.add_child(textBox1)

# Traverse and execute components
# Use the iterator for traversal
for component in window:
    component.get_name()
    component.execute()
```

## Benefits

1. Tree-like Structure:

It allows for the creation of hierarchical structures, where objects can contain other objects.
This simplifies the representation of complex, nested structures.

2. Uniform Treatment of Objects:

It treats both individual objects and compositions of objects uniformly.
This reduces code complexity and promotes code reuse.

3. Flexible Design:

It allows for the dynamic addition and removal of components.
This makes the system adaptable to changes and extensions.

4. Simplified Iteration:

It simplifies the traversal of complex structures using iterative patterns.
This reduces the need for recursion or manual traversal.

5. Enhanced Code Readability:

It promotes a clear and concise design by separating concerns.
This makes the code easier to understand and maintain.

## Use Cases:

1. File System:

Represents files and directories as components.
Allows for recursive traversal and operations on files and directories.

2. GUI Components:

Organizes GUI components into hierarchical structures (e.g., panels, windows, menus).
Enables consistent handling of individual components and groups of components.

3. Document Structure:

Represents documents as a tree of components (e.g., paragraphs, headings, lists).
Allows for flexible document formatting and rendering.

4. Organizational Charts:

Models hierarchical organizational structures, where employees can be both individuals and managers of teams.

5. Network Protocols:

Represents network protocols as a tree of packets and headers.

6. Compiler Design:

Represents the abstract syntax tree (AST) of a program as a hierarchical structure.

## Summary

The Composite Pattern is a structural design pattern that allows you to treat individual objects and compositions of objects uniformly. It's particularly useful for creating hierarchical structures, like GUI components, file systems, or organizational charts.
