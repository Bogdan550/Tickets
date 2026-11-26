from Seats import BusinessSeat, ComfortSeat, EconomySeat
from random import choice, randint
class Plane:
    def __init__(self):
        self.name = self.made_name()
        self.es = self.made_ES()
        self.bs = self.made_BS(self.es)
        self.cs = self.made_CS(self.es)

    @staticmethod
    def made_name():
        names = ["samoletik", "sushka", "kartina", "dagar"]
        return choice(names)

    @staticmethod
    def made_BS(es):
        if es  <= 180:
            return randint(6, 12)
        elif es <= 220:
            return randint(13, 20)
        return randint(20, 28)

    @staticmethod
    def made_CS(es):
        if es <= 150:
            return randint(0, 18)
        elif es <= 220:
            return randint(10, 30)
        return randint(20, 40)

    @staticmethod
    def made_ES():
        return randint(100, 270)

    def free_bs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"

    def free_cs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"

    def free_es(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"