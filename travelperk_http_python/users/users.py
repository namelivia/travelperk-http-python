from typing import TYPE_CHECKING
from .users_query import UsersQuery

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class Users:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    # Query users.
    def query(self) -> UsersQuery:
        return UsersQuery(self.travelperk)
