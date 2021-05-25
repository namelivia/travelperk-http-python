from typing import TYPE_CHECKING
from travelperk_http_python.trips.trips import Trips
from travelperk_http_python.trips.bookings import Bookings

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class TripsAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._trips = Trips(travelperk)
        self._bookings = Bookings(travelperk)

    def trips(self) -> Trips:
        return self._trips

    def bookings(self) -> Bookings:
        return self._bookings
