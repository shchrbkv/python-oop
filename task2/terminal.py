import os

from pizza import Pepperoni, BBQ, Seafood
from order import Order


class Terminal:
    menu = [Pepperoni(), BBQ(), Seafood()]
    __code = 0

    def greet(self):
        os.system("clear")
        print("{:^40}".format("Welcome to Pizza Time"))

    def boot(self):
        self.greet()
        print("{:^40}".format("Is it a takeout? y/n"))
        current_order = Order(self.__code, True) if input() == "y" or "Y" else Order(self.__code)

        while True:
            self.greet()
            print("{:^40}".format("Order #" + str(current_order.code)))

            print("Choose your pizza:")
            for p in range(len(self.menu)):
                print("{} - {}".format(p+1, self.menu[p].title))
            print("Enter the id of pizza, or 0 to finish")
            chosen = int(input())

            if chosen in range(len(self.menu)+1):
                if chosen == 0:
                    break
                chosen_pizza = self.menu[chosen - 1]
                current_order.add(chosen_pizza)
                chosen_pizza.bake()
                chosen_pizza.pack()
            else:
                continue

            print(current_order)
            print("\n1 - Choose another\n0 - Finish the order")

            if input() == "1":
                continue
            else:
                break

        self.__code += 1
