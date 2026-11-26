class Flight:
    def __init__(self, plane, time_out, time_in, number):
        self.plane = plane
        self.time_out = time_out
        self.time_in = time_in
        self.number = number
    def get_info(self):
        return self.number, self.plane.name, self.time_out, self.time_in
