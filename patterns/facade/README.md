# Facade Pattern

## Definition

The Facade Pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

### Complex SubSystems

    ```python
    class Amplifier:
        def on(self):
            print("Amplifier turned on")

        def set_input_source(self, source):
            print(f"Amplifier input source set to {source}")

        def set_surround_sound_mode(self):
            print("Amplifier set to surround sound mode")

        def set_volume(self, level):
            print(f"Amplifier volume set to {level}")

        def off(self):
            print("Amplifier turned off")

    class Projector:
        def on(self):
            print("Projector turned on")

        def wide_screen_mode(self):
            print("Projector in wide screen mode")

        def off(self):
            print("Projector turned off")

    class Lights:
        def dim(self, level):
            print(f"Lights dimmed to {level}%")

        def brighten(self, level):
            print(f"Lights brightened to {level}%")

    class BluRayPlayer:
        def on(self):
            print("Blu-ray player turned on")

        def open_tray(self):
            print("Blu-ray player tray opened")

        def play(self):
            print("Blu-ray player playing")

        def stop(self):
            print("Blu-ray player stopped")

        def close_tray(self):
            print("Blu-ray player tray closed")

        def off(self):
            print("Blu-ray player turned off")

    class CableBox:
        def on(self):
            print("Cable box turned on")

        def tune_channel(self, channel):
            print(f"Cable box tuned to channel {channel}")

        def off(self):
            print("Cable box turned off")
    ```

### Simplified Facade System

    ```python
    class HomeTheaterFacade:
        def __init__(self, amplifier, projector, lights, blu_ray_player, cable_box):
            self.amplifier = amplifier
            self.projector = projector
            self.lights = lights
            self.blu_ray_player = blu_ray_player
            self.cable_box = cable_box

        def watch_movie(self):
            print("Watch Movie:")
            self.lights.dim(10)
            self.projector.on()
            self.projector.wide_screen_mode()
            self.amplifier.on()
            self.amplifier.set_input_source("DVD")
            self.amplifier.set_surround_sound_mode()
            self.amplifier.set_volume(5)
            self.blu_ray_player.on()
            self.blu_ray_player.open_tray()
            self.blu_ray_player.play()

        def watch_tv(self):
            print("Watch TV:")
            self.lights.dim(10)
            self.projector.on()
            self.projector.wide_screen_mode()
            self.amplifier.on()
            self.amplifier.set_input_source("TV")
            self.amplifier.set_volume(5)
            self.cable_box.on()
            self.cable_box.tune_channel(5)

        def end_activity(self):
            print("End Activity:")
            self.blu_ray_player.stop()
            self.blu_ray_player.close_tray()
            self.blu_ray_player.off()
            self.cable_box.off()
            self.amplifier.set_volume(0)
            self.amplifier.off()
            self.projector.off()
            self.lights.brighten(100)

    amplifier = Amplifier()
    projector = Projector()
    lights = Lights()
    blu_ray_player = BluRayPlayer()
    cable_box = CableBox()

    home_theater = HomeTheaterFacade(amplifier, projector, lights, blu_ray_player, cable_box)

    home_theater.watch_movie()
    home_theater.end_activity()
    home_theater.watch_tv()
    home_theater.end_activity()
    ```

## Benefits

- Simplified Interface: The facade class provides a simple interface to control the complex system.
- Loose Coupling: The facade class decouples the client from the complex subsystems. This means that changes to the underlying subsystems can be made without affecting the facade class or the client code.
- Improved Maintainability: The facade class can be updated to accommodate new devices or features without affecting the existing client code.
- Reduced Complexity: The facade hides the complexity of the underlying subsystems, making the system easier to understand and use.
- Reusability: The facade can be reused in different contexts, such as a smart home system or a commercial theater.

## Use Case

The Facade Pattern is a versatile design pattern that can be applied in various scenarios. Here are some common use cases:

1. Complex Subsystem Simplification

   - Home Theater System: As demonstrated in the previous example, the Facade Pattern can simplify the control of complex home theater systems.

   - Database Systems: A Facade can provide a simplified interface for interacting with a complex database system, hiding the underlying SQL queries and database connections.

2. Legacy System Integration

   - Legacy APIs: A Facade can wrap a legacy API with a more modern interface, making it easier to integrate with new systems.

3. Third-Party Library Abstraction

   - Complex Libraries: A Facade can provide a simpler interface to a complex third-party library, hiding its internal complexities.

4. Microservices Architecture

   - Service Orchestration: A Facade can be used to orchestrate multiple microservices, providing a unified interface to clients.

5. GUI Toolkits

   - Abstraction Layer: A Facade can provide a simplified interface to a complex GUI toolkit, making it easier to use and customize.

By using the Facade Pattern, you can improve the usability, maintainability, and flexibility of your software systems.

## Summary

The Facade Pattern is a structural design pattern that simplifies complex systems by providing a unified interface. It hides the complexity of underlying subsystems, making them easier to use and understand.
