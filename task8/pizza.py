from abc import ABC, abstractmethod


class Pizza(ABC):
    title = ""
    dough = ""
    sauce = ""
    cost = 0

    def __init__(self, cost):
        self.cost = round(cost, 2)

    def prepare(self):
        self.bake()
        self.pack()

    @abstractmethod
    def bake(self):
        pass

    def pack(self, takeout):
        if takeout:
            return "Packing {} in a box...".format(self.title)
        else:
            return "Nicely putting {} on a plate...".format(self.title)


class Pepperoni(Pizza):
    def __init__(self, cost):
        self.title = "Pepperoni"
        self.dough = "1-day"
        self.sauce = "Marinara"
        self.__topping = ["Cheese", "Pepperoni"]
        super().__init__(cost)

    def bake(self):
        return(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 9 minutes!")


class BBQ(Pizza):
    def __init__(self, cost):
        self.title = "BBQ"
        self.dough = "3-day"
        self.sauce = "Marinara"
        self.__topping = ["Cheese", "Pork", "Sausages"]
        super().__init__(cost)

    def bake(self):
        return(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 15 minutes!")


class Seafood(Pizza):
    def __init__(self, cost):
        self.title = "Seafood"
        self.dough = "3-day"
        self.sauce = "White"
        self.__topping = ["Clams", "Shrimps", "Squid"]
        super().__init__(cost)

    def bake(self):
        return(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 20 minutes!")