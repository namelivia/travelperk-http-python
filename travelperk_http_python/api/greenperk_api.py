from typing import TYPE_CHECKING
from travelperk_http_python.greenperk.greenperk import GreenPerk

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class GreenPerkAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._greenperk = GreenPerk(travelperk)

    def greenperk(self) -> GreenPerk:
        return self._greenperk
