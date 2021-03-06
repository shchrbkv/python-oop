import time


class HandoutMeta(type):
    def __new__(cls, name, bases, dct):
        dct["location_of_pickup"] = dct["locationOfPickupPoint"]
        dct.pop("locationOfPickupPoint")
        print(dct)
        return type(name, bases, dct)


def with_stats(method):
    def get_stats(self, takeout):
        print("### Initializing task {} ###".format(method.__name__))
        start = time.time()
        method(self, takeout)
        end = time.time()
        print("### Completed task '{}' in {:.2f} seconds ###".format(method.__name__, end - start))
    return get_stats


class Handout(metaclass=HandoutMeta):
    locationOfPickupPoint = "near the coffee machine"

    @with_stats
    def pack(self, takeout):
        if takeout:
            print("Packing {} in a box...".format(self.title))
            time.sleep(2)
        else:
            print("Nicely putting {} on a plate...".format(self.title))
            time.sleep(1)
