from mock import Mock
from travelperk_http_python.api.cost_centers_api import CostCentersAPI
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.cost_centers.cost_centers import CostCenters


class TestCostCenters:
    def setup_method(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.cost_centers = CostCentersAPI(self.travelperk)

    def test_getting_a_cost_centers_instance(self):
        assert type(self.cost_centers.cost_centers()) is CostCenters
