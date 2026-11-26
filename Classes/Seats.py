class Seat:
    def __init__(self):
        self.taken = False
        self.price = None

    def take_seat(self):
        self.taken = not self.taken

    def get_seat(self):
        return self.taken

    def get_price(self):
        return self.price


class BusinessSeat(Seat):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def get_price(self):
        return self.price


class ComfortSeat(Seat):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def get_price(self):
        return self.price


class EconomySeat(Seat):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def get_price(self):
        return self.price
