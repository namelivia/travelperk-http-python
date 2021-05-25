import datetime
from typing import TYPE_CHECKING
from travelperk_python_api_types.trips.trips.trips import Trips
from .trips_input_params import TripsInputParams

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class TripsQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = TripsInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        return getattr(self.travelperk, method)(url, params)

    def get(self) -> Trips:
        return Trips(
            **self.execute(
                "get", "/".join(["trips"]) + "?" + self.params.as_url_param()
            )
        )

    def set_status(self, status: str) -> "TripsQuery":
        self.params.set_status(status)
        return self

    def set_modified_lt(self, modified_lt: datetime) -> "TripsQuery":
        self.params.set_modified_lt(modified_lt)
        return self

    def set_modified_gte(self, modified_gte: datetime) -> "TripsQuery":
        self.params.set_modified_lt(modified_gte)
        return self

    def set_offset(self, offset: int) -> "TripsQuery":
        self.params.set_offset(offset)
        return self

    def set_limit(self, limit: int) -> "TripsQuery":
        self.params.set_limit(limit)
        return self
