# Super or Base Class
from abc import ABC, abstractmethod
from random import randint


class IFlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class IQuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass


class GenericFlight(IFlyBehaviour):
    def fly(self):
        print("I'm Flying!")


class AdvancedFlight(IFlyBehaviour):
    def fly(self):
        print("I'm Flying Even Higher!")


class NonFlight(IFlyBehaviour):
    def fly(self):
        print("I'm Not Flying and I Tried!")


class GenericQuack(IQuackBehaviour):
    def quack(self):
        print("I'm Quacking Hard!")


class GenericSqueak(IQuackBehaviour):
    def quack(self):
        print("I'm Definitely Not Quacking!")
        
class NonSound(IQuackBehaviour):
    def quack(self):
        print("I'm Not Making a Sound!")


class DuckSuperClass:
    
    def __init__(self, flight_behaviour: IFlyBehaviour, quack_behaviour: IQuackBehaviour) -> None:
        self.FLIGHT_BEHAVIOUR = flight_behaviour
        self.QUACK_BEHAVIOUR = quack_behaviour
        
    def set_flight(self, flight: IFlyBehaviour):
        self.FLIGHT_BEHAVIOUR = flight
    
    def set_quack(self, quack: IQuackBehaviour):
        self.QUACK_BEHAVIOUR = quack
    
    def execute_flight(self):
        if not self.FLIGHT_BEHAVIOUR or not isinstance(
            self.FLIGHT_BEHAVIOUR, IFlyBehaviour
        ):
            NonFlight().fly()
        else:
            self.FLIGHT_BEHAVIOUR.fly()

    def execute_quack(self):
        if not self.QUACK_BEHAVIOUR or not isinstance(
            self.QUACK_BEHAVIOUR, IQuackBehaviour
        ):
            NonSound().quack()
        else:
            self.QUACK_BEHAVIOUR.quack()

    def swim(self):
        print("Swimming Hard!")

    def display(self):
        print("Im a Duck!")


class MallardDuck(DuckSuperClass):
    def __init__(self) -> None:
        super().__init__(GenericFlight(), GenericQuack())
        self.FLIGHT = AdvancedFlight()

    # Overrides Duck Display Trait
    def display(self):
        print("Im a Mallard Duck!")


class RedHeadDuck(DuckSuperClass):
    def __init__(self) -> None:
        super().__init__(AdvancedFlight(), GenericQuack())
        self.FLIGHT = GenericFlight()
        

    def display(self):
        print("Im a Red-Head Duck!")


class RubberDuck(DuckSuperClass):
    def __init__(self) -> None:
        super().__init__(NonFlight(), GenericSqueak())
        self.FLIGHT = AdvancedFlight()
        

    def display(self):
        print("Im a Rubber Duck!")


class Dog(DuckSuperClass):
    def __init__(self) -> None:
        super().__init__(None, None)
        self.FLIGHT = NonFlight()
        
        
    def Display(self):
        print("I'm a Dog!")


md = MallardDuck()
rhd = RedHeadDuck()
rd = RubberDuck()
d = Dog()

for duck in (md, rhd, rd, d):
    duck.display()
    duck.execute_quack()
    duck.swim()
    duck.execute_flight()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    duck.set_flight((NonFlight(), GenericFlight(), AdvancedFlight())[randint(0, 2)])
    duck.set_quack((GenericQuack(), GenericSqueak(), NonSound())[randint(0, 2)])
    duck.display()
    duck.execute_quack()
    duck.swim()
    duck.execute_flight()
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    
