from typing import TYPE_CHECKING
from travelperk_python_api_types.greenperk.greenperk.emissions import Emissions
from travelperk_python_api_types.greenperk.greenperk.hotel_emissions import (
    HotelEmissions,
)
from .flight_emissions_params import FlightEmissionsParams
from .train_emissions_params import TrainEmissionsParams
from .hotel_emissions_params import HotelEmissionsParams
from .car_emissions_params import CarEmissionsParams
from dataclass_map_and_log.mapper import DataclassMapper

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class GreenPerk:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    # Get emissions for flight.
    def flight_emissions(
        self, origin: str, destination: str, cabin_class: str, airline_code: str
    ) -> Emissions:
        params = FlightEmissionsParams(origin, destination, cabin_class, airline_code)

        return DataclassMapper.map(
            Emissions,
            self.execute(
                "get",
                "/".join(["emissions", "flight"]) + "?" + params.as_url_param(),
            ),
        )

    # Get emissions for train.
    def train_emissions(
        self, origin_id: str, destination_id: str, vendor: str = None
    ) -> Emissions:
        params = TrainEmissionsParams(origin_id, destination_id, vendor)

        return DataclassMapper.map(
            Emissions,
            self.execute(
                "get",
                "/".join(["emissions", "train"]) + "?" + params.as_url_param(),
            ),
        )

    # Get emissions for car.
    def car_emissions(
        self, acriss_code: str, num_days: int, distance_per_day: int = None
    ) -> Emissions:
        params = CarEmissionsParams(acriss_code, num_days, distance_per_day)

        return DataclassMapper.map(
            Emissions,
            self.execute(
                "get",
                "/".join(["emissions", "car"]) + "?" + params.as_url_param(),
            ),
        )

    # Get emissions for hotel.
    def hotel_emissions(self, country_code: str, num_nights: int) -> Emissions:
        params = HotelEmissionsParams(country_code, num_nights)

        return DataclassMapper.map(
            HotelEmissions,
            self.execute(
                "get",
                "/".join(["emissions", "hotel"]) + "?" + params.as_url_param(),
            ),
        )
