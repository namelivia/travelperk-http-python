import datetime
import urllib
from .location_type import LocationType


class TravelRestrictionParams:
    def __init__(
        self,
        origin: str,
        destination: str,
        origin_type: str,
        destination_type: str,
        date: datetime,
    ):
        self.set_origin(origin)
        self.set_destination(destination)
        self.set_origin_type(origin_type)
        self.set_destination_type(destination_type)
        self.set_date(date)

    def set_origin(self, origin: str) -> "TravelRestrictionParams":
        self.origin = origin
        return self

    def set_destination(self, destination: str) -> "TravelRestrictionParams":
        self.destination = destination
        return self

    def set_origin_type(self, origin_type: str) -> "TravelRestrictionParams":
        self.origin_type = LocationType(origin_type)
        return self

    def set_destination_type(self, destination_type: str) -> "TravelRestrictionParams":
        self.destination_type = LocationType(destination_type)
        return self

    def set_date(self, date: datetime) -> "TravelRestrictionParams":
        self.date = date
        return self

    def as_url_param(self) -> str:
        return urllib.parse.urlencode(
            {
                "origin": self.origin,
                "destination": self.destination,
                "origin_type": self.origin_type.value,
                "destination_type": self.destination_type.value,
                "date": self.date.strftime("%Y-%m-%d"),
            }
        )
