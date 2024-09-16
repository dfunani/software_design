from abc import abstractmethod, ABC
from enum import Enum
from typing import List


class Pizzas(Enum):
    pass


class PizzaException(Exception):
    pass


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]

    def prepare(self):
        list_of_toppings = "\n".join(
            [
                f"    {index}. {topping}"
                for index, topping in enumerate(self.toppings, 1)
            ]
        )
        print(
            f"""Preparing {self.name}
Rolling Out Dough to Make a {self.dough} Base
Adding Layer of {self.sauce} Sauce
Adding Toppings:
{list_of_toppings}
"""
        )
        self.pizza.append("Prepared")

    def bake(self):
        print("Baked for 15 minutes at 150°C")
        self.pizza.append("Baked")

    def cut(self):
        print("Cut Diagonally into 8 Slices - Triangular")
        self.pizza.append("Cut")

    def box(self):
        print("Boxed Pizza - Square")
        self.pizza.append("Boxed")


class CheesePizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "Regular Cheese Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class PepperoniPizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "Regular Pepperoni Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class NYStyleCheesePizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "New York Style Cheese Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class NYStylePepperoniPizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "New York Style Pepperoni Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "Chicago Style Cheese Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, factory: "PizzaIngredientFactory") -> None:
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = factory.create_dough()
        self.sauce = factory.create_sauce()
        self.toppings = factory.create_toppings()
        self.pizza = []


class StandardPizzas(Pizzas):
    CHEESEPIZZA = CheesePizza
    PEPPERONIPIZZA = PepperoniPizza


class NYStylePizzas(Pizzas):
    CHEESEPIZZA = NYStyleCheesePizza
    PEPPERONIPIZZA = NYStylePepperoniPizza


class ChicagoStylePizzas(Pizzas):
    CHEESEPIZZA = ChicagoStyleCheesePizza
    PEPPERONIPIZZA = ChicagoStylePepperoniPizza


class PizzaStore(ABC):
    def order_pizza(self, pizza: Pizzas):
        pizza = self.create_pizza(pizza)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    @abstractmethod
    def create_pizza(self, pizza: Pizzas):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza: Pizzas):
        if not isinstance(pizza, NYStylePizzas):
            raise PizzaException("Invalid NY Pizza")
        return pizza.value(NYStyleIngredientFactory(pizza))


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza: Pizzas):
        if not isinstance(pizza, ChicagoStylePizzas):
            raise PizzaException("Invalid Chicago Pizza")
        return pizza.value(ChicagoIngredientStyleFactory(pizza))


class PizzaIngredientFactory(ABC):
    def __init__(self, pizza: Pizzas) -> None:
        self.pizza = pizza

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_toppings(self):
        pass


class StandardIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Normal"

    def create_sauce(self):
        return "Marinara"

    def create_toppings(self):
        if self.pizza == StandardPizzas.CHEESEPIZZA:
            return ["Cheese"]
        if self.pizza == StandardPizzas.PEPPERONIPIZZA:
            return ["Cheese", "Pepperoni"]
        return []


class NYStyleIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Thin"

    def create_sauce(self):
        return "Marinara"

    def create_toppings(self):
        if self.pizza == NYStylePizzas.CHEESEPIZZA:
            return ["Cheese"]
        if self.pizza == NYStylePizzas.PEPPERONIPIZZA:
            return ["Cheese", "Pepperoni", "Garlic"]
        return []


class ChicagoIngredientStyleFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Thick"

    def create_sauce(self):
        return "BBQ"

    def create_toppings(self):
        if self.pizza == ChicagoStylePizzas.CHEESEPIZZA:
            return ["Cheese", "Ranch"]
        if self.pizza == ChicagoStylePizzas.PEPPERONIPIZZA:
            return ["Cheese", "Pepperoni", "Ranch"]
        return []


class SimplePizzaStore:
    def order_pizza(self, pizza: Pizzas):
        pizza = simple_pizza_factory(pizza)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


def simple_pizza_factory(pizza: Pizzas) -> Pizza:
    if not isinstance(pizza, Pizzas):
        raise PizzaException("Invalid Pizza")
    return pizza.value(StandardIngredientFactory(pizza))


print(f"{'='*5} Ordering Simple Pizza {'='*5}")
pizza = SimplePizzaStore()
pizza.order_pizza(StandardPizzas.CHEESEPIZZA)

print(f"{'='*5} NY Store: Ordering Pizza {'='*5}")
pizza = NYPizzaStore()
pizza.order_pizza(NYStylePizzas.PEPPERONIPIZZA)

print(f"{'='*5} Chicago Store: Ordering Pizza {'='*5}")
pizza = ChicagoPizzaStore()
pizza.order_pizza(ChicagoStylePizzas.CHEESEPIZZA)