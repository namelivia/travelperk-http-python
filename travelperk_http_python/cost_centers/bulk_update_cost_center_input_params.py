from typing import List


class BulkUpdateCostCenterInputParams:
    def set_ids(self, ids: List[int]) -> "BulkUpdateCostCenterInputParams":
        self.ids = ids
        return self

    def set_archive(self, archive: bool) -> "BulkUpdateCostCenterInputParams":
        self.archive = archive
        return self

    def to_dict(self) -> dict:
        data = {
            "id_list": self.ids,
            "archive": self.archive,
        }
        return {k: v for k, v in data.items() if v is not None}
