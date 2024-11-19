from abc import ABC, abstractmethod
from typing import Iterator


class IFileSystem(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(IFileSystem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class Directory(IFileSystem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_name(self):
        return self.name

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def __iter__(self) -> Iterator[IFileSystem]:
        return iter(self.children)


# Usage:
root_directory = Directory("Root")
music_directory = Directory("Music")
documents_directory = Directory("Documents")
text_file = File("report.txt", 1024)
image_file = File("photo.jpg", 512)

root_directory.add_child(music_directory)
root_directory.add_child(documents_directory)
music_directory.add_child(image_file)
documents_directory.add_child(text_file)

# Traverse and print information
for item in root_directory:
    print(item.get_name(), item.get_size())
