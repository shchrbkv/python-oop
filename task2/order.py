class Order:
    order_list = []
    __total = 0

    def __init__(self, code, takeout=False):
        self.__code = code
        self.takeout = takeout

    @property
    def code(self):
        return self.__code

    def add(self, pizza):
        self.order_list.append(pizza)
        self.__total += pizza.cost

    def get_total(self):
        return self.__total

    def __str__(self):
        return "\n{0} items for a total of ${1:.2f}".format(len(self.order_list), self.get_total())
