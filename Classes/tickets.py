from Plane import Plane
from Flight import Flight
class Tickets:
    def __init__(self, flights = []):
        self.flights = flights

    def add_flight(self):
        pl = Plane()
        time_out = None
        time_in = None
        prices = None
        fl = Flight(pl, time_out, time_in, prices)
    def run(self):
        pass