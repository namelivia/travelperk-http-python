from typing import List, TYPE_CHECKING
from .status import Status
from .trips_query import TripsQuery

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class Trips:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    # Query trips.
    def query(self) -> TripsQuery:
        return TripsQuery(self.travelperk)

    # Get all statuses.
    def statuses(self) -> List[str]:
        return Status.getConstantValues()
