import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.greenperk.greenperk import GreenPerk


class TestGreenPerk:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.greenperk = GreenPerk(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def test_getting_flight_emissions(self):
        self.travelperk.get.return_value = self.get_stub_contents("emissions.json")
        emissions = self.greenperk.flight_emissions("BCN", "LHR", "economy", "BA")
        self.travelperk.get.assert_called_once_with(
            "emissions/flight?origin=BCN&destination=LHR&cabin_class=economy&airline_code=BA"
        )
        assert emissions.emissions.CO2e_kg == 21
        assert emissions.distance_km == 200

    def test_getting_train_emissions(self):
        self.travelperk.get.return_value = self.get_stub_contents("emissions.json")
        emissions = self.greenperk.train_emissions(
            "c44ba069-4109-4b40-815c-bf519c2c2844",
            "637d125e-9d00-478a-822c-e60c6e219227",
            "eurostar",
        )
        self.travelperk.get.assert_called_once_with(
            "emissions/train?origin_id=c44ba069-4109-4b40-815c-bf519c2c2844&destination_id=637d125e-9d00-478a-822c-e60c6e219227&vendor=eurostar"
        )
        assert emissions.emissions.CO2e_kg == 21
        assert emissions.distance_km == 200

    def test_getting_car_emissions(self):
        self.travelperk.get.return_value = self.get_stub_contents("emissions.json")
        emissions = self.greenperk.car_emissions("MCFD", 2, 100)
        self.travelperk.get.assert_called_once_with(
            "emissions/car?acriss_code=MCFD&num_days=2&distance_per_day=100"
        )
        assert emissions.emissions.CO2e_kg == 21
        assert emissions.distance_km == 200

    def test_getting_hotel_emissions(self):
        self.travelperk.get.return_value = self.get_stub_contents("emissions.json")
        emissions = self.greenperk.hotel_emissions("ES", 2)
        self.travelperk.get.assert_called_once_with(
            "emissions/hotel?country_code=ES&num_nights=2"
        )
        assert emissions.emissions.CO2e_kg == 21
