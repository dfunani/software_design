# Adapter Pattern

## Definition

The Adapter Pattern converts the interface of a class into another interface the clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

### Home Automation - Adapter

1. Target Interface (ISmartPlug)

   ```python
   from abc import ABC, abstractmethod
   from enum import Enum

   class States(Enum):
       ON = "On"
       OFF = "Off"

   class ISmartPlug(ABC):
       def __init__(self, name: str):
           self.name = name
           self.state = States.OFF

       @abstractmethod
       def On(self):
           pass

       @abstractmethod
       def Off(self):
           pass
   ```

2. Adaptee Interface (IThermostat)

   ```python
   class IThermostat(ABC):
       def __init__(self, name: str):
           self.name = name
           self.temperature = 18  # Initial temperature

       @abstractmethod
       def increase(self):
           pass

       @abstractmethod
       def decrease(self):
           pass
   ```

3. Adapter (ThermostatAdapter)

   ```python
   class ThermostatAdapter(ISmartPlug):
       def __init__(self, thermostat: IThermostat):
           self.thermostat = thermostat

       def On(self):
           print(f"{self.thermostat.name} (Thermostat Adapter): Increasing temperature")
           self.thermostat.increase()  # Increase temperature to simulate "On"

       def Off(self):
           print(f"{self.thermostat.name} (Thermostat Adapter): Decreasing temperature")
           self.thermostat.decrease()  # Decrease temperature to simulate "Off"
   ```

4. Concrete Target Implementation (SmartControlPanel)

   ```python
   class SmartControlPanel(ISmartPlug):
       def On(self):
           self.state = States.ON
           print(f"{self.name} (Smart Control Panel): Turned on")  # Explicit on action

       def Off(self):
           self.state = States.OFF
           print(f"{self.name} (Smart Control Panel): Turned off")  # Explicit off action
   ```

5. Concrete Adaptee Implementation (ClassicThermostat)

   ```python
   class ClassicThermostat(IThermostat):
       def increase(self):
           self.temperature += 1
           print(f"{self.name} (Classic Thermostat): Temperature increased to {self.temperature}")

       def decrease(self):
           self.temperature -= 1
           print(f"{self.name} (Classic Thermostat): Temperature decreased to {self.temperature}")
   ```

6. Create concrete device instances

```python
smart_plug = SmartControlPanel("Living Room Plug")
thermostat = ClassicThermostat("Main Thermostat")
thermostat_adapter = ThermostatAdapter(thermostat)  # Adapt thermostat to smart plug interface

# Simulate user interactions using the common ISmartPlug interface
print("Turning on Smart Plug:")
smart_plug.On()

print("\nTurning on Thermostat (using adapter):")
thermostat_adapter.On()

print("\nTurning off Thermostat (using adapter):")
thermostat_adapter.Off()

print("\nTurning off Smart Plug:")
smart_plug.Off()
```

## Benefits

- Flexibility: The system can easily accommodate new devices by creating adapters for their specific protocols.
- Reusability: Existing devices can be integrated without modifying their core functionality.
- Maintainability: The adapter isolates the complexity of device-specific interactions, making the system easier to maintain.

## Use Case

The Adapter Pattern is a versatile design pattern that can be applied in various scenarios. Here are some common use cases:

- Legacy System Integration: Bridging the gap between old and new systems.
- Third-Party Library Integration: Adapting third-party libraries to fit your system's needs.
- Hardware Abstraction: Creating a unified interface for various hardware devices.
- Data Format Conversion: Converting data between different formats.
- GUI Toolkit Integration: Adapting GUI tool-kits to work with your application.

By applying the Adapter Pattern, you can make your software more flexible, reusable, and maintainable. It allows you to integrate different systems and components that would otherwise be incompatible, promoting a more modular and adaptable architecture.

## Summary

The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together. It involves creating an adapter class that translates requests from one interface to another, enabling seamless integration between different components or systems.
