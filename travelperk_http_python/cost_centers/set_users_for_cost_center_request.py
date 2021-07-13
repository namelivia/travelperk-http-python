from typing import List, TYPE_CHECKING
from .set_users_for_cost_center_input_params import SetUsersForCostCenterInputParams
from travelperk_python_api_types.cost_centers.cost_centers.cost_center_detail import (
    CostCenterDetail,
)

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class SetUsersForCostCenterRequest:
    def __init__(self, id: str, travelperk: "TravelPerk"):
        self.params = SetUsersForCostCenterInputParams()
        self.id = id
        self.travelperk = travelperk

    def save(self) -> CostCenterDetail:
        return CostCenterDetail(
            **self.travelperk.put(
                "/".join(["cost_centers", self.id, "users"]), self.params.to_dict()
            )
        )

    def set_ids(self, ids: List[int]) -> "SetUsersForCostCenterRequest":
        self.params.set_ids(ids)
        return self
