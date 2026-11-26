from Seats import BusinessSeat, ComfortSeat, EconomySeat
class Plane:
    def __init__(self, name, BS, CS, ES):
        self.name = name
        self.bs = BS
        self.cs = CS
        self.es = ES
    def free_bs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"
    def free_cs(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"
    def free_es(self):
        f = len((i for i in self.bs if not i.get_taken()))
        return f"{f}/{len(self.bs)}"