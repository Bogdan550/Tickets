class Seat:
    def __init__(self):
        self.taken = False
    def take_seat(self):
        self.taken = not self.taken

class FirstClassSeat(Seat):
    pass

class BusinessClassSeat(Seat):
    pass