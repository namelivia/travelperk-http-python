from typing import TYPE_CHECKING
from .update_cost_center_input_params import UpdateCostCenterInputParams
from travelperk_python_api_types.cost_centers.cost_centers.cost_center_detail import (
    CostCenterDetail,
)

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class UpdateCostCenterRequest:
    def __init__(self, id: int, travelperk: "TravelPerk"):
        self.id = id
        self.params = UpdateCostCenterInputParams()
        self.travelperk = travelperk

    def save(self) -> CostCenterDetail:
        return CostCenterDetail(
            **self.travelperk.patch(
                "/".join(["cost_centers", str(self.id)]), self.params.to_dict()
            )
        )

    def set_name(self, name: str) -> "UpdateCostCenterRequest":
        self.params.set_name(name)
        return self

    def set_archive(self, archive: bool) -> "UpdateCostCenterRequest":
        self.params.set_archive(archive)
        return self
