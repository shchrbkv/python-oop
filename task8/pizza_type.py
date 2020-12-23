from abc import ABC, abstractmethod
import pizza as pizzas


class PizzaType(ABC):
    name = ""

    def __init__(self, name):
        self.name = name

    def get_type(self):
        return self.name + " pizza section"

    @abstractmethod
    def create(self, pizza, price):
        pass


class ItalianPizzaType(PizzaType):
    def __init__(self, name):
        super().__init__(name)

    def create(self, name, price):
        if name == "Pepperoni":
            return pizzas.Pepperoni(price)


class ExoticPizzaType(PizzaType):
    def __init__(self, name):
        super().__init__(name)

    def create(self, name, price):
        if name == "BBQ":
            return pizzas.BBQ(price)
        elif name == "Seafood":
            return pizzas.Seafood(price)

