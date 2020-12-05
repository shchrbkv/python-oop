from abc import ABC, abstractmethod
from handout import Handout
import time


def with_stats(method):
    def get_stats(*args):
        print("### Initializing task '{}' ###".format(method.__name__))
        start = time.time()
        method(*args)
        end = time.time()
        print("### Completed task '{}' in {:.2f} seconds ###".format(method.__name__, end - start))
    return get_stats


class Pizza(Handout, ABC):
    title = ""
    dough = ""
    sauce = ""
    cost = 0

    @abstractmethod
    def bake(self):
        pass


class Pepperoni(Pizza):
    def __init__(self):
        self.title = "Pepperoni"
        self.dough = "1-day"
        self.sauce = "Marinara"
        self.__topping = ["Cheese", "Pepperoni"]
        self.cost = 4.20

    @with_stats
    def bake(self):
        print(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 9 minutes!")
        time.sleep(5)


class BBQ(Pizza):
    def __init__(self):
        self.title = "BBQ"
        self.dough = "3-day"
        self.sauce = "Marinara"
        self.__topping = ["Cheese", "Pork", "Sausages"]
        self.cost = 6.90

    def bake(self):
        print(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 15 minutes!")

class Seafood(Pizza):
    def __init__(self):
        self.title = "Seafood"
        self.dough = "3-day"
        self.sauce = "White"
        self.__topping = ["Clams", "Shrimps", "Squid"]
        self.cost = 3.22

    def bake(self):
        print(self.title + " pizza / " +
              self.dough + " dough / " +
              self.sauce + " sauce - is baking for 20 minutes!")
