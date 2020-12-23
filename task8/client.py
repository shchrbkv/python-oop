from terminal import Terminal, StartScreen


class Client:
    def __init__(self, code):
        self.terminal = Terminal(code)

    def start(self):
        self.terminal.segue_to(StartScreen())

