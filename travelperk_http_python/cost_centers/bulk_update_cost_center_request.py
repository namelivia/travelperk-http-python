from typing import List, TYPE_CHECKING
from .bulk_update_cost_center_input_params import BulkUpdateCostCenterInputParams
from travelperk_python_api_types.cost_centers.cost_centers.bulk_update_response import (
    BulkUpdateResponse,
)

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class BulkUpdateCostCenterRequest:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = BulkUpdateCostCenterInputParams()
        self.travelperk = travelperk

    def save(self) -> BulkUpdateResponse:
        return BulkUpdateResponse(
            **self.travelperk.patch(
                "/".join(["cost_centers", "bulk_update"]),
                self.params.to_dict(),
            )
        )

    def set_ids(self, ids: List[int]) -> "BulkUpdateCostCenterRequest":
        self.params.set_ids(ids)
        return self

    def set_archive(self, archive: bool) -> "BulkUpdateCostCenterRequest":
        self.params.set_archive(archive)
        return self
