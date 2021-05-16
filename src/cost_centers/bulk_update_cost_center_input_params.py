from typing import List


class BulkUpdateCostCenterInputParams:
    def set_ids(self, ids: List[int]) -> "BulkUpdateCostCenterInputParams":
        self.ids = ids
        return self

    def set_archive(self, archive: bool) -> "BulkUpdateCostCenterInputParams":
        self.archive = archive
        return self

    def to_dict(self) -> dict:
        # TODO: Look for the best way to clean None values from a dict
        return {
            "id_list": self.ids,
            "archive": self.archive,
        }
