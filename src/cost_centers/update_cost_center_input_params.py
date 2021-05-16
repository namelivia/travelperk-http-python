class UpdateCostCenterInputParams:
    def set_name(self, name: str) -> "UpdateCostCenterInputParams":
        self.name = name
        return self

    def set_archive(self, archive: bool) -> "UpdateCostCenterInputParams":
        self.archive = archive
        return self

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "archive": self.archive,
        }
