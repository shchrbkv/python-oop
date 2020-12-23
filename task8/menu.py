import os
from aiofile import async_open
import asyncio
from pizza_type import ItalianPizzaType, ExoticPizzaType
from singleton import SingletonMeta


class Menu(metaclass=SingletonMeta):
    raw = []
    menu = []
    italian = ItalianPizzaType("Italian")
    exotic = ExoticPizzaType("Exotic")

    async def get_data(self):
        async with async_open(os.path.dirname(__file__) + "/available.txt", "r") as raw:
            self.raw = (await raw.read()).split(" ")

    def preprocess(self, item):
        values = {
            "type": "",
            "title": "",
            "price": 0
        }
        data = item.split(":")
        values["type"] = data[0]
        values["title"] = data[1]
        values["price"] = float(data[2])
        return values

    def update(self):
        asyncio.run(self.get_data())
        for item in self.raw:
            data = self.preprocess(item)
            if data["type"] == "italian":
                self.menu.append(self.italian.create(data["title"], data["price"]))
            elif data["type"] == "exotic":
                self.menu.append(self.exotic.create(data["title"], data["price"]))
        return self.menu


class LocalPreprocessors:
    def preprocess_us(self, item):
        values = {
            "type": "",
            "title": "",
            "price": 0
        }
        data = item.split(":")
        print(data)
        values["type"] = data[0]
        values["title"] = data[1]
        values["price"] = float(data[2])*0.8 #in US dollars
        return values


class MenuAdapter(Menu, LocalPreprocessors):
    def update(self):
        print(self.raw)
        asyncio.run(self.get_data())
        for item in self.raw:
            data = self.preprocess_us(item)
            if data["type"] == "italian":
                self.menu.append(self.italian.create(data["title"], data["price"]))
            elif data["type"] == "exotic":
                self.menu.append(self.exotic.create(data["title"], data["price"]))
        return self.menu

