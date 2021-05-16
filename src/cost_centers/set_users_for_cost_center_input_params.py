from typing import List


class SetUsersForCostCenterInputParams:
    def set_ids(self, ids: List[int]) -> "SetUsersForCostCenterInputParams":
        self.ids = ids
        return self

    def to_dict(self) -> dict:
        return {"user_ids": self.ids}
