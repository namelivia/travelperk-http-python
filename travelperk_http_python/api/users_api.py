from typing import TYPE_CHECKING
from travelperk_http_python.users.users import Users

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class UsersAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._users = Users(travelperk)

    def users(self) -> Users:
        return self._users
