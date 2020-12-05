import os
import threading
import asyncio
from aiofile import async_open
from tkinter import *

# Local imports
from pizza import Pepperoni, BBQ, Seafood
from order import Order
from handout import Handout


async def check_availability():
    async with async_open(os.path.dirname(__file__) + "/available.txt", "r") as raw:
        return (await raw.read()).split(" ")


class Terminal:
    menu = {"Pepperoni": Pepperoni(),
            "BBQ": BBQ(),
            "Seafood": Seafood()}
    screen = 0
    log_history = ""

    def __init__(self):
        self.window = Tk()
        self.window.title("Pizza Time Terminal")
        self.window.geometry("480x240")
        self.window.configure()

        header = Label(self.window, text="Welcome to Pizza Time!", font=("Helvetica", 27, "bold"),
                       pady="20")

        self.status_text = StringVar()
        self.status_text.set("Is it a takeout?")
        status = Label(self.window, textvariable=self.status_text, font=("Helvetica", 20))

        self.pizzas = Frame(self.window)

        self.log_text = StringVar()
        self.log = Label(self.window, textvariable=self.log_text, font=("Helvetica", 16, "italic"),
                    fg="grey", anchor="s")

        navbar = Frame(width="5")
        self.main = Button(navbar, text="Yes", command=lambda: self.set_current_order(True),
                           width="100", font=("Helvetica", 20), pady="10")
        self.secondary = Button(navbar, text="No", command=lambda: self.set_current_order(False),
                                width="100", font=("Helvetica", 20), pady="10")

        header.pack(side=TOP)
        status.pack(side=TOP)

        self.pizzas.pack(side=TOP)


        self.main.pack()
        self.secondary.pack()
        navbar.pack(side=BOTTOM)
        self.log.pack(side=BOTTOM)

    def update_status(self, message):
        self.status_text.set(message)

    def update_pizzas(self):
        available = []

        for pizza in asyncio.run(check_availability()):
            available.append(self.menu[pizza])

        for widget in self.pizzas.winfo_children():
            widget.destroy()

        Label(self.pizzas, text="CHOOSE YOUR PIZZA", pady="3",
              font=("Helvetica", 16, "bold")).pack(pady="10")
        for pizza in available:
            pizza_button = Button(self.pizzas, command=lambda p=pizza: self.select_pizza(p),
                   text="{} - ${}".format(pizza.title, pizza.cost),
                   width="20", pady=10, font=("Helvetica", 20, "bold"))
            pizza_button.pack(pady="5")

    def update_navbar(self):
        if self.screen == 1:
            self.window.geometry("480x640")
            self.update_pizzas()
            self.main.config(text="Proceed to checkout", command=self.checkout)
            self.secondary.config(text="Cancel the order", command=self.reset)
        if self.screen == 2:
            self.window.geometry("480x240")
            self.main.config(text="Create another order", command=self.reset)
            self.secondary.config(text="Exit the terminal", command=self.window.destroy)

    def set_current_order(self, takeout):
        self.current_order = Order(self.__code, takeout)
        self.screen = 1
        self.log.configure(height="5", pady="20")
        self.update_navbar()
        self.update_status(self.current_order)

    def select_pizza(self, pizza):
        try:
            self.current_order.add(pizza)

            if len(self.current_order.order_list) > 4:
                self.update_status(self.current_order.__str__() + "\n DISCOUNT 20%")
            else:
                self.update_status(self.current_order)

            packing = threading.Thread(target=pizza.pack, args=(self.current_order.takeout,))
            baking = threading.Thread(target=pizza.bake)

            baking.start()
            packing.start()

            baking.join()
            self.update_log("{} pizza is baked!".format(pizza.title))
            packing.join()
            self.update_log("{} pizza is packed!".format(pizza.title))
        except Exception as e:
            self.update_log(e.__str__())

    def update_log(self, message):
        self.log_history += "\n" + message
        self.log_text.set(self.log_history)

    def start(self, code):
        self.__code = code
        self.window.mainloop()

    def checkout(self):
        self.screen = 2
        self.update_status("Order #{} is ready.\nYou can pick up your order {}".format(self.__code,
                                                                                      Handout.location_of_pickup))
        self.pizzas.destroy()
        self.log.destroy()
        self.update_navbar()
        self.__code += 1

    def reset(self):
        self.window.destroy()
        self.__init__()
        self.screen = 0
        self.log_history = ""
