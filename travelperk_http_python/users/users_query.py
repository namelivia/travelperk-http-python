from typing import TYPE_CHECKING
from .users_input_params import UsersInputParams
from travelperk_python_api_types.users.users.users import Users

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class UsersQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = UsersInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    def get(self) -> Users:
        return Users(
            **self.execute(
                "get",
                "/".join(["users"]) + "?" + self.params.as_url_param(),
            )
        )

    def set_trip_id(self, trip_id: str) -> "UsersQuery":
        self.params.set_trip_id(trip_id)
        return self

    def set_offset(self, offset: int) -> "UsersQuery":
        self.params.set_offset(offset)
        return self

    def set_limit(self, limit: int) -> "UsersQuery":
        self.params.set_limit(limit)
        return self
