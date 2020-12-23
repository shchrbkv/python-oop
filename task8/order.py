from exceptions import PizzaOverload, PizzaDiscount


class Order:
    __total = 0

    def __init__(self, code, takeout=False):
        self.__code = code
        self.takeout = takeout
        self.order_list = []

    @property
    def code(self):
        if self.__code >= 0:
            return self.__code % 100
        else:
            return self.__code

    def add(self, pizza):
        self.order_list.append(pizza)
        if len(self.order_list) > 10:
            raise PizzaOverload(len(self.order_list))
        self.__total += pizza.cost

    def get_total(self):
        current_total = self.__total
        try:
            if len(self.order_list) > 4:
                raise PizzaDiscount
        except PizzaDiscount as e:
            current_total *= 0.8
        finally:
            return current_total

    def __str__(self):
        return "[{}] Order #{}\n{} items for a total of ${:.2f}".format("Takeout" if self.takeout else "Inhouse",
                                                                        self.code,
                                                                        len(self.order_list),
                                                                        self.get_total())

