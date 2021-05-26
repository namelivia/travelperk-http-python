from travelperk_http_python.scim.name_input_params import NameInputParams


class UpdateUserInputParams:
    def __init__(self):
        self.user_name = None
        self.active = None
        self.name = None

    def set_user_name(self, user_name: str) -> "UpdateUserInputParams":
        self.user_name = user_name
        return self

    def set_active(self, active: bool) -> "UpdateUserInputParams":
        self.active = active
        return self

    def set_name(self, name: NameInputParams) -> "UpdateUserInputParams":
        self.name = name
        return self

    def to_dict(self) -> dict:
        data = {
            "userName": self.user_name,
            "name": self.name.to_dict() if self.name is not None else None,
            "active": self.active,
        }
        return {k: v for k, v in data.items() if v is not None}
