class Flight:
    def __init__(self, plane, time_out, time_in, prices):
        self.plane = plane
        self.time_out = time_out
        self.time_in = time_in
        self.prices = prices

    def get_info(self):
        return self.plane, self.time_out, self.time_in, self.prices
