# Singleton Pattern

## Definition

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This prevents multiple instances of the class from being created, which can lead to inconsistencies or unexpected behavior.

### Logger - Singleton

We define a Logger Service that will manage all logging. Only one can exist at any given time.

```python
from enum import Enum
from datetime import datetime

class Levels(Enum):
    INFO = "info"
    DEBUG = "debug"

class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def info(self, message: str):
        self.__log(Levels.INFO, message)

    def debug(self, message: str):
        self.__log(Levels.DEBUG, message)

    def __log(self, level: Levels, message: str):
        print(f"[{datetime.now().strftime('%d/%M/%Y %H:%m:%S')}] {__name__} - {level.value} - {message}")

logger1 = Logger()
logger1.info("Hello World!")
logger2 = Logger()
logger2.info("Hello World!")
print(logger1 is logger2)```
```

## Use Case

The Singleton Pattern is valuable in scenarios where you need to ensure that a class has only one instance throughout the application, providing a global point of access to that instance. This is useful for managing shared resources, controlling access to critical data, or implementing global configuration settings.

## Summary

A singleton class acts as a central authority, guaranteeing that there's only one instance of itself. This prevents multiple instances from being created, which can lead to inconsistencies or unexpected behavior. Other parts of the application can access this single instance to interact with the shared resource or configuration.
