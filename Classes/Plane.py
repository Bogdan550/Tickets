from Seats import BusinessSeat, ComfortSeat, EconomySeat
from random import choice, randint
class Plane:
    def __init__(self):
        self.name = self.made_name()
        self.bs = self.made_BS()
        self.cs = self.made_CS()
        self.es = self.made_ES()
    @staticmethod
    def made_name():
        names = ["samoletik", "sushka"]
        return choice(names)

    @staticmethod
    def made_BS():
        return randint(2, 16)

    @staticmethod
    def made_CS():
        return randint(0, 28)

    @staticmethod
    def made_ES():
        return randint(150, 250)
    def free_bs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"
    def free_cs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"
    def free_es(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"