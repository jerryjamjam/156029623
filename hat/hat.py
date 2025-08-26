import random


class Hat:
    houses = ["griffin", "raven", "huff", "slither"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
