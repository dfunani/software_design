from abc import ABC, abstractmethod
from typing import List, Tuple


class IBeverage(ABC):
    __description__: str = []
    __discount__: int = 0.0

    @abstractmethod
    def price(self) -> float:
        pass
    
    @property
    @abstractmethod
    def description(self) -> List[Tuple[str, int]]:
        pass

    @property
    @abstractmethod
    def discount(self) -> float:
        pass

class Espresso(IBeverage):
    def __init__(self) -> None:
        self.__discount__ = 0.0
        self.__price__ = 20
        self.__description__.append(["Espresso", self.__price__ * (1 - self.__discount__)])
        
    @property
    def description(self) -> List[Tuple[str, int]]:
        return self.__description__

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.__price__ * (1 - self.__discount__)

class HouseBlend(IBeverage):
    def __init__(self) -> None:
        self.__discount__ = 0.0
        self.__price__ = 18
        self.__description__.append(["House Blend", self.__price__ * (1 - self.__discount__)])
        
    @property
    def description(self) -> List[Tuple[str, int]]:
        return self.__description__

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.__price__ * (1 - self.__discount__)
    
    
class DarkRoast(IBeverage):
    def __init__(self) -> None:
        self.__discount__ = 0.0
        self.__price__ = 19
        self.__description__.append(["Dark Roast", self.__price__ * (1 - self.__discount__)])
        
    @property
    def description(self) -> List[Tuple[str, int]]:
        return self.__description__

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.__price__ * (1 - self.__discount__)
    
class Decaf(IBeverage):
    def __init__(self) -> None:
        self.__discount__ = 0.0
        self.__price__ = 20
        self.__description__.append(["Decaf", self.__price__ * (1 - self.__discount__)])
        
    @property
    def description(self) -> List[Tuple[str, int]]:
        return self.__description__

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.__price__ * (1 - self.__discount__)
    

class ICondiment(IBeverage):
    pass

class SteamMilk(ICondiment):
    def __init__(self, beverage: IBeverage) -> None:
        self.beverage = beverage
        self.__discount__ = 0.0
        self.__price__ = 5
        
    @property
    def description(self) -> str:
        return self.beverage.description + [["Steamed Milk", self.__price__ * (1 - self.__discount__)]]

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.beverage.price() + (self.__price__ * (1 - self.__discount__))
    
class Mocha(ICondiment):
    def __init__(self, beverage: IBeverage) -> None:
        self.beverage = beverage
        self.__discount__ = 0.0
        self.__price__ = 10
        
    @property
    def description(self) -> str:
        return self.beverage.description + [["Mocha", self.__price__ * (1 - self.__discount__)]]

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.beverage.price() + (self.__price__ * (1 - self.__discount__))
    
class Soy(ICondiment):
    def __init__(self, beverage: IBeverage) -> None:
        self.beverage = beverage
        self.__discount__ = 0.0
        self.__price__ = 7.5
        
    @property
    def description(self) -> str:
        return self.beverage.description + [["Soy", self.__price__ * (1 - self.__discount__)]]

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.beverage.price() + (self.__price__ * (1 - self.__discount__))
    
class Whip(ICondiment):
    def __init__(self, beverage: IBeverage) -> None:
        self.beverage = beverage
        self.__discount__ = 0.0
        self.__price__ = 5
        
    @property
    def description(self) -> str:
        return self.beverage.description + [["Whipped", self.__price__ * (1 - self.__discount__)]]

    @property
    def discount(self) -> float:
        return self.__discount__
    
    @discount.setter
    def discount(self, value: float) -> None:
        self.__discount__ = float(value)

    def price(self) -> float:
        return self.beverage.price() + (self.__price__ * (1 - self.__discount__))

print("===================== Here is Your Receipt =====================") 
drink = Whip(Espresso())
drink.discount = 0.5
max_price = max([len(str(price)) for _, price in drink.description])
max_desc = max([len(desc) for desc, _ in drink.description])
print(f"{"\n".join([f"{description:{max_desc}}  {price}" for description, price in drink.description])}\n{" ":{max_desc}}  {"-"*max_price}\n{"Total":{max_desc}}  {drink.price()}")
