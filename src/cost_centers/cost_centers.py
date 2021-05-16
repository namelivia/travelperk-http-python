from typing import List, TYPE_CHECKING

from cost_centers.cost_centers.cost_centers import CostCenters as CostCentersType
from cost_centers.cost_centers.cost_center_detail import CostCenterDetail
from .update_cost_center_request import UpdateCostCenterRequest
from .bulk_update_cost_center_request import BulkUpdateCostCenterRequest
from .set_users_for_cost_center_request import SetUsersForCostCenterRequest

if TYPE_CHECKING:
    from src.api.travelperk import TravelPerk


class CostCenters:
    def __init__(self, travelperk: "TravelPerk"):  # , JsonMapper $mapper)
        self.travelperk = travelperk
        # $this->mapper = $mapper;

    # TODO: This is temporary
    def execute(self, method: str, url: str, _class: str, params: List = None):
        # TODO: This is for doing the type mapping
        # I'll see how do I sort this out
        """
        # TODO: The return value will be an instance of the providen class
        $result = new $class();
        """
        if params is None:
            response = getattr(self.travelperk, method)(url)
        else:
            response = getattr(self.travelperk, method)(url, params)
        """
        #TODO: And here the mapping from the response to the object is done
        $this->mapper->mapObject(
            json_decode($response),
            $result
        );
        """

        # return result
        return response

    # List all cost centers.
    def all(self) -> CostCentersType:
        return self.execute("get", "/".join(["cost_centers"]), "CostCentersType")

    # Get cost center detail.
    def get(self, id: str) -> CostCenterDetail:
        return self.execute("get", "/".join(["cost_centers", id]), "CostCenterDetail")

    # Update the cost center endpoint.
    def modify(self, id: str) -> UpdateCostCenterRequest:
        return UpdateCostCenterRequest(id, self.travelperk)

    # Bulk update an several cost centers at once.
    def bulk_update(self) -> BulkUpdateCostCenterRequest:
        return BulkUpdateCostCenterRequest(self.travelperk)

    # Set the users for a cost center.
    def set_users(self, id: str) -> SetUsersForCostCenterRequest:
        return SetUsersForCostCenterRequest(id, self.travelperk)
