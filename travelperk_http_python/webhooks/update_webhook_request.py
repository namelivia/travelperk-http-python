from typing import TYPE_CHECKING, List
from .update_webhook_input_params import UpdateWebhookInputParams
from travelperk_python_api_types.webhooks.webhooks.webhook import Webhook

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class UpdateWebhookRequest:
    def __init__(self, id: str, travelperk: "TravelPerk"):
        self.id = id
        self.params = UpdateWebhookInputParams()
        self.travelperk = travelperk

    def save(self) -> Webhook:
        return Webhook(
            **self.travelperk.patch(
                "/".join(["webhooks", self.id]), self.params.to_dict()
            )
        )

    def set_name(self, name: str) -> "UpdateWebhookRequest":
        self.params.set_name(name)
        return self

    def set_enabled(self, enabled: bool) -> "UpdateWebhookRequest":
        self.params.set_enabled(enabled)
        return self

    def set_url(self, url: str) -> "UpdateWebhookRequest":
        self.params.set_url(url)
        return self

    def set_secret(self, secret: str) -> "UpdateWebhookRequest":
        self.params.set_secret(secret)
        return self

    def set_events(self, events: List[str]) -> "UpdateWebhookRequest":
        self.params.set_events(events)
        return self
