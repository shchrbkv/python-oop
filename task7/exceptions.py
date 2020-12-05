class PizzaOverload(Exception):
    def __init__(self, pizza_count):
        self.pizza_count = pizza_count

    def __str__(self):
        return "Oops, guess 10 pizzas is the limit! Proceed to checkout!"


class PizzaDiscount(Exception):
    def __str__(self):
        return "Congratulations! You have 5 pizzas in your cart and get a 20% discount!"
