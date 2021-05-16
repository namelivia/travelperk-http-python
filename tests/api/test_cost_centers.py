from mock import Mock
from src.api.cost_centers_api import CostCentersAPI
from src.api.travelperk import TravelPerk
from src.cost_centers.cost_centers import CostCenters


class TestCostCenters:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.cost_centers = CostCentersAPI(self.travelperk)

    def test_getting_a_cost_centers_instance(self):
        assert type(self.cost_centers.cost_centers()) is CostCenters
