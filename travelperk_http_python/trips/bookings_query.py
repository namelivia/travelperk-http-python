import datetime
from typing import TYPE_CHECKING
from .bookings_input_params import BookingsInputParams
from travelperk_python_api_types.trips.bookings.bookings import Bookings

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class BookingsQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = BookingsInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        return getattr(self.travelperk, method)(url, params)

    def get(self) -> Bookings:
        return Bookings(
            **self.execute(
                "get",
                "/".join(["bookings"]) + "?" + self.params.as_url_param(),
            )
        )

    def set_trip_id(self, trip_id: str) -> "BookingsQuery":
        self.params.set_trip_id(trip_id)
        return self

    def set_status(self, status: str) -> "BookingsQuery":
        self.params.set_status(status)
        return self

    def set_type(self, _type: str) -> "BookingsQuery":
        self.params.setType(_type)
        return self

    def set_modified_lt(self, modified_lt: datetime) -> "BookingsQuery":
        self.params.set_modified_lt(modified_lt)
        return self

    def set_modified_gte(self, modified_gte: datetime) -> "BookingsQuery":
        self.params.set_modified_gte(modified_gte)
        return self

    def set_offset(self, offset: int) -> "BookingsQuery":
        self.params.set_offset(offset)
        return self

    def set_limit(self, limit: int) -> "BookingsQuery":
        self.params.set_limit(limit)
        return self
