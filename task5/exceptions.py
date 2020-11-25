class PizzaOverload(Exception):
    def __init__(self, pizza_count):
        self.pizza_count = pizza_count

    def __str__(self):
        return "10 pizzas is the maximum (you tried {})".format(self.pizza_count)


class PizzaDiscount(Exception):
    def __str__(self):
        return "Congratulations! You have 5 pizzas in your cart and get a 20% discount!"
