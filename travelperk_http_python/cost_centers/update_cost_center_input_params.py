class UpdateCostCenterInputParams:
    def __init__(self):
        self.name = None
        self.archive = None

    def set_name(self, name: str) -> "UpdateCostCenterInputParams":
        self.name = name
        return self

    def set_archive(self, archive: bool) -> "UpdateCostCenterInputParams":
        self.archive = archive
        return self

    def to_dict(self) -> dict:
        data = {
            "name": self.name,
            "archive": self.archive,
        }
        return {k: v for k, v in data.items() if v is not None}
