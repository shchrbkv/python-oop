import os

from pizza import Pepperoni, BBQ, Seafood
from order import Order
from handout import Handout

class Terminal:
    menu = [Pepperoni(), BBQ(), Seafood()]

    def greet(self):
        os.system("clear")
        print("{:-^40}".format("Welcome to Pizza Time"))

    def start(self, code):
        self.__code = code
        self.greet()
        print("{:^40}".format("Is it a takeout? y/n"))
        current_order = Order(self.__code, True) if input() == ("y" or "Y") else Order(self.__code)

        while True:
            self.greet()
            print(current_order)
            print("\nChoose your pizza:")
            for p in range(len(self.menu)):
                position = self.menu[p]
                print("{} - ${:.2f} - {}".format(p+1, position.cost, position.title))
            print("Enter the id of pizza, or 0 to finish")
            chosen = int(input())

            if chosen in range(len(self.menu)+1):
                if chosen == 0:
                    break
                chosen_pizza = self.menu[chosen - 1]
                current_order.add(chosen_pizza)
                chosen_pizza.bake()
                chosen_pizza.pack(current_order.takeout)
            else:
                continue

            print("\n1 - Choose another\n0 - Finish the order")

            if input() == "1":
                continue
            else:
                break

        self.greet()
        print(current_order)
        print("Proceed to checkout...")
        print("You can pick up your order " + Handout.location_of_pickup) # !
        self.__code += 1
