from abc import ABC, abstractmethod
from tkinter import *
from order import Order
from menu import MenuAdapter
from log import Log


class Terminal:
    _screen = None

    def __init__(self, code):
        #Initialize Tk
        self.window = Tk()
        self.window.title("Pizza Time Terminal")
        self.window.configure()

        #Common elements
        header = Label(self.window, text="Welcome to Pizza Time!",
                       font=("Helvetica", 27, "bold"), pady="20")

        self.status_text = StringVar()
        self.status_text.set("hi")
        print(self.status_text)
        status = Label(self.window, textvariable=self.status_text, font=("Helvetica", 20))

        self.pizzas = Frame(self.window)
        self.log_text = StringVar()
        self.log_ui = Label(self.window, textvariable=self.log_text, font=("Helvetica", 16, "italic"),
                         fg="grey", anchor="s")
        navbar = Frame(width="5")
        self.main = Button(navbar, text="", width="100", font=("Helvetica", 20), pady="10")
        self.secondary = Button(navbar, text="", width="100", font=("Helvetica", 20), pady="10")

        #Packing
        header.pack(side=TOP)
        status.pack(side=TOP)

        self.pizzas.pack(side=TOP)

        self.main.pack()
        self.secondary.pack()
        navbar.pack(side=BOTTOM)
        self.log_ui.pack(side=BOTTOM)

        #Variables set
        self.log = Log()
        self._code = code
        self.takeout = False

    # Code
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    def segue_to(self, screen):
        self._screen = screen
        self._screen.terminal = self
        self.update_ui()

    def update_ui(self):
        self._screen.update_ui()

    def update_log(self, message):
        self._screen.update_log(message)


class Screen(ABC):
    _terminal = None

    @property
    def terminal(self):
        return self._terminal

    @terminal.setter
    def terminal(self, terminal: Terminal):
        self._terminal = terminal

    @abstractmethod
    def update_ui(self):
        pass

    @abstractmethod
    def update_log(self, message):
        pass


class StartScreen(Screen):
    def __init__(self):
        pass

    def update_ui(self):
        self.terminal.window.geometry("480x240")
        self.terminal.status_text.set("Is it a takeout?")
        self.terminal.main.config(text="Yes", command=lambda: self.button_action(True))
        self.terminal.secondary.config(text="No", command=lambda: self.button_action(False))
        self.terminal.window.mainloop()

    def update_log(self, message):
        pass

    def button_action(self, takeout):
        self.terminal.takeout = takeout
        self.terminal.segue_to(OrderScreen())


class OrderScreen(Screen):
    def __init__(self):
        pass

    def update_ui(self):
        self.current_order = Order(self.terminal.code, self.terminal.takeout)
        self.terminal.log_ui.configure(height="5", pady="20")
        self.terminal.window.geometry("480x640")
        self.terminal.status_text.set(self.current_order)
        self.terminal.main.config(text="Proceed to checkout", command=lambda: self.terminal.segue_to(CheckoutScreen()))
        self.terminal.secondary.config(text="Cancel the order", command=lambda: self.terminal.segue_to(CheckoutScreen()))
        self.update_pizza_list()

    def update_pizza_list(self):
        menu = MenuAdapter()
        available = menu.update()
        print(available)

        for widget in self.terminal.pizzas.winfo_children():
            widget.destroy()

        Label(self.terminal.pizzas, text="CHOOSE YOUR PIZZA", pady="3",
              font=("Helvetica", 16, "bold")).pack(pady="10")
        for pizza in available:
            pizza_button = Button(self.terminal.pizzas, command=lambda p=pizza: self.select_pizza(p),
                                  text="{} - ${}".format(pizza.title, pizza.cost),
                                  width="20", pady=10, font=("Helvetica", 20, "bold"))
            pizza_button.pack(pady="5")

    def select_pizza(self, pizza):
        try:
            self.current_order.add(pizza)

            if len(self.current_order.order_list) > 4:
                self.terminal.status_text.set(self.current_order.__str__() + "\n DISCOUNT 20%")
            else:
                self.terminal.status_text.set(self.current_order)

            self.update_log(pizza.bake())
            self.update_log("{} pizza is baked!".format(pizza.title))

            self.update_log(pizza.pack(self.terminal.takeout))
            self.update_log("{} pizza is packed!".format(pizza.title))

        except Exception as e:
            self.update_log(e.__str__())

    def update_log(self, message):
        self.terminal.log.write(message)
        self.terminal.log_text.set(self.terminal.log.history)


class CheckoutScreen(Screen):
    def __init__(self):
        pass

    def update_ui(self):
        self.terminal.status_text.set("Order #{} is ready.\nPut on your face mask and gloves"
                                      " to pickup the order.".format(self.terminal.code))
        self.terminal.pizzas.destroy()
        self.terminal.log_ui.destroy()
        self.terminal.window.geometry("640x240")
        self.terminal.main.config(text="Create another order", command=lambda: self.terminal.segue_to(StartScreen()))
        self.terminal.secondary.config(text="Exit the terminal", command=self.terminal.window.destroy)
        self.terminal.code += 1

    def update_log(self, message):
        self.terminal.log.write("\n\n\n\n\n\n")

