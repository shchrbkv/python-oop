from singleton import SingletonMeta
import datetime


class Log(metaclass=SingletonMeta):
    def __init__(self):
        self._history = "Log started:" + str(datetime.date.today())

    @property
    def history(self):
        return self._history

    def write(self, message):
        self._history += "\n" + message

