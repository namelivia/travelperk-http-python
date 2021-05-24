from typing import TYPE_CHECKING
from travelperk_http_python.scim.users import Users
from travelperk_http_python.scim.discovery import Discovery

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class SCIMAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._users = Users(travelperk)
        self._discovery = Discovery(travelperk)

    def users(self) -> Users:
        return self._users

    def discovery(self) -> Discovery:
        return self._discovery
