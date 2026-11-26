from random import randint
class Flight:
    def __init__(self, plane, prices):
        self.plane = plane
        time = self.time(plane.bs + plane.es + plane.cs)
        self.time_out = time[0]
        self.time_in =  time[1]
        self.prices = prices

    @staticmethod
    def time(s):
        time_out = [randint(0, 23), randint(0,59)]
        time_in = [None, randint(0,59)]
        if s < 200:
            dif = randint(1, 4)
        else:
            dif = randint(3, 7)
        time_in[0] = (time_out[0] + dif) % 24
        return f"{time_out[0]}:{time_out[1]}", f"{time_in[0]}:{time_in[1]}"


    def get_info(self):
        return self.plane, self.time_out, self.time_in, self.prices
