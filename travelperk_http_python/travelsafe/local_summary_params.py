import urllib
from .location_type import LocationType


class LocalSummaryParams:
    def __init__(self, location: str, location_type: str):
        self.set_location(location)
        self.set_location_type(location_type)

    def set_location(self, location: str) -> "LocalSummaryParams":
        self.location = location
        return self

    def set_location_type(self, location_type: str) -> "LocalSummaryParams":
        self.location_type = LocationType(location_type)
        return self

    def as_url_param(self) -> str:
        return urllib.parse.urlencode(
            {
                "location_type": self.location_type.value,
                "location": self.location,
            }
        )
