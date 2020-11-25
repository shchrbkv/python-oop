class Pizza:
    title = ""
    dough = ""
    sauce = ""

    def pack(self):
        print(self.title + " is being packed!")


class Pepperoni(Pizza):
    def __init__(self):
        self.title = "Pepperoni"
        self.dough = "1-day"
        self.sauce = "Red"
        self.__topping = ["Cheese", "Pepperoni"]
        self.cost = 4.20

    def bake(self):
        print(self.title +" / "+ self.dough +" / "+ self.sauce + " is baking for 9 minutes!")


class BBQ(Pizza):
    def __init__(self):
        self.title = "BBQ"
        self.dough = "3-day"
        self.sauce = "Red"
        self.__topping = ["Cheese", "Pork", "Sausages"]
        self.cost = 6.90

    def bake(self):
        print(self.title +" / "+ self.dough +" / "+ self.sauce + " is baking for 15 minutes!")


class Seafood(Pizza):
    def __init__(self):
        self.title = "Seafood"
        self.dough = "3-day"
        self.sauce = "White"
        self.__topping = ["Clams", "Shrimps", "Squid"]
        self.cost = 3.22

    def bake(self):
        print(self.title +" / "+ self.dough +" / "+ self.sauce + " is baking for 20 minutes!")
