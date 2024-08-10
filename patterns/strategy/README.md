# Strategy Pattern

## Definition:

The Strategy Pattern defines a family of behaviors or algorithms, allowing them to be used interchangeably based on the desired composition. This pattern is particularly useful when an object needs to change its behavior at runtime.

### 1. Character (Extended) - Inheritance Section

We define a base class Character and extend it to create specific types of characters like *Hero*, *Villain*, and *Troll*.

```python
class Character:
    def display(self):
        print("I'm a Character")

class Hero(Character):
    pass

class Villain(Character):
    pass

class Troll(Character):
    pass

# Demonstrating that all sub-characters can access the display method.
Hero().display()  # Output: I'm a Character
Villain().display()  # Output: I'm a Character
Troll().display()  # Output: I'm a Character
```

### 2. IWeaponBehaviour (Implemented) - Composition Section

We define an interface IWeaponBehaviour and implement it with different weapon behaviors like *GunBehaviour*, *SwordBehaviour*, and *KnifeBehaviour*.

```python
from abc import ABC, abstractmethod

class IWeaponBehaviour(ABC):
    @abstractmethod
    def attack(self):
        pass

class GunBehaviour(IWeaponBehaviour):
    def attack(self):
        print("Shoot Shoot!")

class SwordBehaviour(IWeaponBehaviour):
    def attack(self):
        print("Swoosh Swoosh!")

class KnifeBehaviour(IWeaponBehaviour):
    def attack(self):
        print("Stab Stab!")
```

The Character class will decide on the WeaponBehaviour to use at runtime by choosing from one of the available strategies. We will use a behavior setter method to change the weapon behavior dynamically.

```python
class Character:
    def __init__(self, weapon_behaviour: IWeaponBehaviour):
        self.weapon_behaviour = weapon_behaviour

    def set_weapon_behaviour(self, weapon_behaviour: IWeaponBehaviour):
        self.weapon_behaviour = weapon_behaviour

    def attack(self):
        self.weapon_behaviour.attack()

class Hero(Character):
    pass

# Runtime: Gun Attack
hero = Hero(GunBehaviour())
hero.attack()  # Output: Shoot Shoot!

# Runtime: Weapon Change to Knife
hero.set_weapon_behaviour(KnifeBehaviour())
hero.attack()  # Output: Stab Stab!
```

## Use Case:

The Strategy Pattern is useful in any program that requires varying behaviors that an object can choose from at runtime. These varying behaviors are encapsulated as algorithms that are distinct and may change over time. This pattern provides flexibility and enables the easy addition of new behaviors without modifying existing code.

## Summary:

By using the Strategy Pattern, we decouple the behavior from the character, making it easier to add new behaviors or modify existing ones without affecting the character's code. This enhances the maintainability and scalability of the system.
````

