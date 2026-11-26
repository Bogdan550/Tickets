from Plane import Plane
from Flight import Flight
class Tickets:
    def __init__(self, flights = []):
        self.flights = flights

    def set_flight(self, flight):
        self.flights.append(flight)
    def run(self):
        pass