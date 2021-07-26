class CreateCostCenterInputParams:
    def __init__(self, name: str):
        self.name = name

    def set_name(self, name: str) -> "CreateCostCenterInputParams":
        self.name = name
        return self

    def to_dict(self) -> dict:
        data = {
            "name": self.name,
        }
        return {k: v for k, v in data.items() if v is not None}
