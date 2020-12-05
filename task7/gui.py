class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pizza Time Terminal")
        self.window.geometry("480x640")

        header = Label(self.window, text="Welcome to Pizza Time!", font=("Helvetica", 27, "bold"), pady="20")

        self.status_text = StringVar()
        self.status_text.set("Is it a takeout?")
        status = Label(self.window, textvariable=self.status_text, font=("Helvetica", 20))

        self.pizzas = Frame(self.window)

        self.navbar = Frame(self.window)

        header.pack(side=TOP)
        status.pack(side=TOP)
        self.pizzas.pack(side=TOP)
        self.navbar.pack(side=TOP)
        self.window.mainloop()

    def update_status(self, message):
        self.status_text.set(message)

    def update_pizzas(self, pizzas, order):
        pizza_buttons = []
        for pizza in pizzas:
            pizza_buttons.append(Button(self.pizzas, command=order.add(pizza),
                                        text="{} - {}".format(pizza.cost, pizza.title),
                                        width="480", font=("Helvetica", 20)))
        for button in pizza_buttons:
            button.pack()

    def update_navbar(self, screen):
        main = Button(self.navbar, text="Yes", width="24", bg="#005555",
                      font=("Helvetica", 20))
        main.pack()
        self.navbar.tkraise()
