class Seat:
    def __init__(self):
        self.__taken = False
        self.__name = None

    def take_seat(self):
        self.__taken = not self.__taken

    def get_taken(self):
        return self.__taken
    def get_name(self):
        return self.__name

class BusinessSeat(Seat):
    def __init__(self, name):
        super().__init__()
        self.name = name

class ComfortSeat(Seat):
    def __init__(self, name):
        super().__init__()
        self.name = name

class EconomySeat(Seat):
    def __init__(self, name):
        super().__init__()
        self.name = name
