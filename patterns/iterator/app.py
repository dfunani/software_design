from abc import ABC, abstractmethod
from typing import Iterator


class IComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Window:
    def __init__(self):
        self.children = []

    def add_child(self, child: IComponent):
        self.children.append(child)

    def __iter__(self) -> Iterator[IComponent]:
        return iter(self.children)


class Button(IComponent):
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def execute(self) -> str:
        return f"Button {self.text} - {self.name} Clicked!"

    def get_name(self) -> str:
        return "I am a (Button)"


class TextBox(IComponent):
    def __init__(self, name, placeholder):
        self.name = name
        self.placeholder = placeholder

    def execute(self) -> str:
        return f"Text-Box {self.placeholder} - {self.name} Input!"

    def get_name(self) -> str:
        return "I am a (TextBox)"


# Usage:
root = Window()
button1 = Button("Button 1", "Click me")
textBox1 = TextBox("Text Box 1", "Enter text")
root.add_child(button1)
root.add_child(textBox1)

for component in root:
    print(component.get_name())
    print(component.execute())
