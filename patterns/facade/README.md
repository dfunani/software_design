# Command Pattern

## Definition

The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations. This separation provides flexibility and allows for:

1. Undo/Redo: Commands can be stored in a history, allowing users to undo or redo actions.
2. Macros: Multiple commands can be grouped together into a single macro, simplifying complex tasks.
3. Queueing: Commands can be queued for execution, providing a non-blocking mechanism for processing requests.
4. Logging: Commands can be logged for auditing or debugging purposes.

### Home Automation - Command

1. Command Interface: Defines a common interface for all commands.

    ```python
    from abc import ABC, abstractmethod

    class ICommand(ABC):
        def __init__(self, receiver: "IReceiver"):
            self.receiver = receiver

        @abstractmethod
        def execute(self):
            pass
    ```

2. Concrete Commands: Implement the Command interface and encapsulate the receiver and the action to be performed.

    ```python
    class DefaultCommand(ICommand):
        def execute(self):
            print("I Am The Default Behaviour!")


    class LightOnCommand(ICommand):
        def execute(self):
            self.receiver.execute(self)


    class LightOffCommand(ICommand):
        def execute(self):
            self.receiver.execute(self)


    class ThermostatUpCommand(ICommand):
        def execute(self):
            self.receiver.execute(self)


    class ThermostatDownCommand(ICommand):
        def execute(self):
            self.receiver.execute(self)
    
    ```

3. Receiver Interface: Defines the interface for objects that can execute commands.

    ```python
    class IReceiver(ABC):
        def __init__(self, name: str):
            self.name = name

        @abstractmethod
        def execute(self):
            pass
    ```

4. Concrete Receivers: Implement the Receiver interface (Devices).

    ```python
    class Light(IReceiver):
        class __STATES(Enum):
            ON = "On"
            OFF = "Off"

        def __init__(self, name: str):
            super().__init__(name)
            self.state = self.__STATES.OFF
        
        def display(self):
            print(f"I am a {self.name} Light - And I am Currently `{self.state}`")

        def execute(self, command: ICommand):
            if isinstance(command, LightOnCommand):
                self.state = self.__STATES.ON.value
            elif isinstance(command, LightOffCommand):
                self.state = self.__STATES.OFF.value

            self.display()


    class Thermostat(IReceiver):
        __TEMP_MAX = 40
        __TEMP_MIN = -20

        def __init__(self, name: str):
            super().__init__(name)
            self.state = 20
        
        def display(self):
            print(f"I am a {self.name} Thermostat - And I am Currently `{self.state}°C`")

        def execute(self, command: ICommand):
            if isinstance(command, ThermostatUpCommand):
                self.state += 1
            elif isinstance(command, ThermostatDownCommand):
                self.state -= 1

            self.state = min(self.state, self.__TEMP_MAX)
            self.state = max(self.__TEMP_MIN, self.state)
            self.display()
    ```

5. Invoker: Holds a reference to a Command object and executes it.

    ```python
    class RemoteControl:
        def __init__(self):
            self.slots = [DefaultCommand(None)] * 7

        def set_command(self, slot, command):
            self.slots[slot] = command

        def press_button(self, slot):
            self.slots[slot].execute()
    ```

6. Client: Creates Concrete Commands and passes them to the Invoker.

    ```python
    living_room_light = Light("Living Room")
    bedroom_thermostat = Thermostat("Bedroom")

    remote = RemoteControl()

    remote.set_command(0, LightOnCommand(living_room_light))
    remote.set_command(1, LightOffCommand(living_room_light))
    remote.set_command(2, ThermostatUpCommand(bedroom_thermostat))
    remote.set_command(3, ThermostatDownCommand(bedroom_thermostat))

    remote.press_button(0)
    remote.press_button(1)
    remote.press_button(2)
    remote.press_button(3)
    remote.press_button(4)
    ```

## Benefits

Decoupling: Separates the invoker from the receiver, improving flexibility and maintainability.
Undo/Redo: Enables users to undo or redo actions.
Macros: Allows for grouping multiple commands into a single action.
Queueing: Provides a non-blocking mechanism for processing commands.
Logging: Facilitates auditing and debugging.

## Use Case

The Command Pattern is valuable in scenarios where you wish to decouple the invoker from the receiver, improving flexibility and maintainability. Providing your program with additional benefits:

1. Undo/Redo: Enables users to undo or redo actions.
2. Macros: Allows for grouping multiple commands into a single action.
3. Queueing: Provides a non-blocking mechanism for processing commands.
4. Logging: Facilitates auditing and debugging.

By applying the Command Pattern, a program can achieve a more modular, flexible, and user-friendly design.

## Summary

The Command Pattern allows decoupling the invoker (button press) from the receiver (light, thermostat) enabling flexibility and features like Undo/Redo, Macros, Queueing, and Logging. It promotes modularity and user-friendliness.