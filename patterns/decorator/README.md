# Decorator Pattern

## Definition:

The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to sub-classing for extending functionality.

### 1. InputStream - Bases Implementations

We define an InputStream and extend it to create specific types of InputStreams _FileInputStream_, _StringBufferInputStream_, _ByteArrayInputStream_ and _FilterInputStream_.

```python
from abc import ABC, abstractmethod

class InputStream(ABC):
    @abstractmethod
    def read(self):
        return "Abstract Base Class, from which Concrete Streams inherit."


# Concrete Classes
class FileInputStream(InputStream):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as file:
            return file.read()

class StringBufferInputStream(InputStream):
    def __init__(self, buffer: str) -> None:
        self.buffer = buffer

    def read(self):
        return self.buffer

class ByteArrayInputStream(InputStream):
    def __init__(self, data: list) -> None:
        self.data = data

    def read(self):
        return self.data
```

### 1. FilterInputStream - Decorator Implementations

We define an FilterInputStream and extend it to create specific types of Input Stream Decorators _BufferedInputStream_, _UpperCaseStream_ and _LowerCaseStream_.

```python
# Decorator Classes
class FilterInputStream(InputStream):
    def read(self):
        return "Decorator Base Class, from which Concrete Decorators inherit. I inherit from the type InputStream"


class BufferedInputStream(FilterInputStream):
    def __init__(self, input_stream: InputStream):
        self.input_stream = input_stream

    def read(self):
        return self.input_stream.read()

class UpperCaseStream(FilterInputStream):
    def __init__(self, input_stream: InputStream):
        self.input_stream = input_stream

    def read(self):
        return self.input_stream.read().lower()


class LowerCaseStream(FilterInputStream):
    def __init__(self, input_stream: InputStream):
        self.input_stream = input_stream

    def read(self):
        return self.input_stream.read().lower()


# Demonstrating that Decorators can be used to add functionality before and/or after the class it wraps.
file_stream = FileInputStream(".gitignore")
buffer_stream = StringBufferInputStream("Hello, world!")
byte_array_stream = ByteArrayInputStream([1, 2, 3])
print(buffer_stream.read(), byte_array_stream.read())

buffered_stream = BufferedInputStream(file_stream)
lower_case_stream = UpperCaseStream(buffered_stream)
upper_case_stream = LowerCaseStream(buffered_stream)

udata = lower_case_stream.read()
ldata = upper_case_stream.read()
print(ldata)
print(udata)
```

## Use Case:

The Decorator Pattern is useful in any program that requires dynamically adding or removing functionalities to objects without modifying their core code. This pattern provides flexibility and enables the easy creation of customized objects and avoids subclass explosion. It's particularly valuable when you need to dynamically adapt the behavior of objects or create customized variations.

## Summary:

By using the Decorator Pattern, we provide a flexible and maintainable way to add additional functionalities to objects without modifying their core code. This pattern enhances the reusability and extensibility of our system. Overall, the Decorator Pattern is a valuable tool for building flexible and adaptable software systems.
