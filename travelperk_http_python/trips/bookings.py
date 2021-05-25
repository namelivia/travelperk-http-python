from typing import List, TYPE_CHECKING
from .bookings_query import BookingsQuery
from .booking_status import BookingStatus
from .type import Type

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class Bookings:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        return getattr(self.travelperk, method)(url, params)

    # Query bookings.
    def query(self) -> BookingsQuery:
        return BookingsQuery(self.travelperk)

    # Get all statuses.
    def statuses(self) -> List[str]:
        return BookingStatus.getConstantValues()

    # Get all types.
    def types(self) -> List[str]:
        return Type.getConstantValues()
