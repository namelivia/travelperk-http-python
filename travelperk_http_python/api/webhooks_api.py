from typing import TYPE_CHECKING
from travelperk_http_python.webhooks.webhooks import Webhooks

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class WebhooksAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._webhooks = Webhooks(travelperk)

    def webhooks(self) -> Webhooks:
        return self._webhooks
