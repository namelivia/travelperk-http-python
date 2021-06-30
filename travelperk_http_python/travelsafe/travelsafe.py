import datetime
from typing import TYPE_CHECKING
from travelperk_python_api_types.travelsafe.restrictions.restriction import Restriction
from travelperk_http_python.travelsafe.travel_restriction_params import (
    TravelRestrictionParams,
)
from travelperk_http_python.travelsafe.local_summary_params import LocalSummaryParams
from travelperk_python_api_types.travelsafe.summary.summary import Summary
from travelperk_python_api_types.travelsafe.airline_measures.airline_measure import (
    AirlineMeasure,
)
from typing import List
from .location_type import LocationType

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class TravelSafe:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    # Provides information about the authorization status and requirements of travel from one location to another.
    def travel_restrictions(
        self,
        origin: str,
        destination: str,
        origin_type: str,
        destination_type: str,
        date: datetime,
    ) -> Restriction:
        params = TravelRestrictionParams(
            origin, destination, origin_type, destination_type, date
        )

        return Restriction(
            **self.execute(
                "get",
                "/".join(["travelsafe", "restrictions"]) + "?" + params.as_url_param(),
            )
        )

    # Retrieve the local summary.
    def local_summary(self, location: str, location_type: str) -> Summary:
        params = LocalSummaryParams(location, location_type)

        return Summary(
            **self.execute(
                "get",
                "/".join(["travelsafe", "guidelines"]) + "?" + params.as_url_param(),
            )
        )

    # Retrieve airline safety measures.
    def airline_safety_measures(self, iata: str) -> AirlineMeasure:
        return AirlineMeasure(
            **self.execute(
                "get",
                "/".join(["travelsafe", "airline_safety_measures"])
                + "?iata_code="
                + iata,
            )
        )

    # Get all location types.
    def location_types(self) -> List[str]:
        return [location_type.value for location_type in LocationType]
