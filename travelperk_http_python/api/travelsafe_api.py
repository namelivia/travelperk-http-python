from typing import TYPE_CHECKING
from travelperk_http_python.travelsafe.travelsafe import TravelSafe

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class TravelSafeAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._travelsafe = TravelSafe(travelperk)

    def cost_centers(self) -> TravelSafe:
        return self._travelsafe
