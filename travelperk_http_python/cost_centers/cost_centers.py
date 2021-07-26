from typing import List, TYPE_CHECKING

from travelperk_python_api_types.cost_centers.cost_centers.cost_centers import (
    CostCenters as CostCentersType,
)
from travelperk_python_api_types.cost_centers.cost_centers.cost_center_detail import (
    CostCenterDetail,
)
from .update_cost_center_request import UpdateCostCenterRequest
from .bulk_update_cost_center_request import BulkUpdateCostCenterRequest
from .set_users_for_cost_center_request import SetUsersForCostCenterRequest

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class CostCenters:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, _class: str = None, params: List = None):
        if params is None:
            response = getattr(self.travelperk, method)(url)
        else:
            response = getattr(self.travelperk, method)(url, params)

        return response

    # List all cost centers.
    def all(self) -> CostCentersType:
        return CostCentersType(**self.execute("get", "/".join(["cost_centers"])))

    # Get cost center detail.
    def get(self, id: int) -> CostCenterDetail:
        return CostCenterDetail(**self.execute("get", "/".join(["cost_centers", id])))

    # Update the cost center endpoint.
    def modify(self, id: int) -> UpdateCostCenterRequest:
        return UpdateCostCenterRequest(id, self.travelperk)

    # Bulk update an several cost centers at once.
    def bulk_update(self) -> BulkUpdateCostCenterRequest:
        return BulkUpdateCostCenterRequest(self.travelperk)

    # Set the users for a cost center.
    def set_users(self, id: int) -> SetUsersForCostCenterRequest:
        return SetUsersForCostCenterRequest(id, self.travelperk)
