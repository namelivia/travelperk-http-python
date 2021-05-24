from typing import TYPE_CHECKING
from travelperk_http_python.cost_centers.cost_centers import CostCenters

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class CostCentersAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._cost_centers = CostCenters(travelperk)

    def cost_centers(self) -> CostCenters:
        return self._cost_centers
