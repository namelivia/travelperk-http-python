from typing import List, TYPE_CHECKING
from .create_webhook_input_params import CreateWebhookInputParams
from .update_webhook_request import UpdateWebhookRequest
from travelperk_python_api_types.webhooks.webhooks.webhook import Webhook
from travelperk_python_api_types.webhooks.webhooks.webhooks import (
    Webhooks as WebhooksType,
)
from travelperk_python_api_types.webhooks.webhooks.event import Event

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class Webhooks:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            return getattr(self.travelperk, method)(url)
        else:
            return getattr(self.travelperk, method)(url, params)

    # List all events you can subscribe to.
    def events(self) -> List[str]:
        events = self.travelperk.get("/".join(["webhooks", "events"]))
        return [Event(**event) for event in events]

    # List all webhook subscriptions.
    def all(self) -> WebhooksType:
        return WebhooksType(**self.execute("get", "/".join(["webhooks"])))

    # Get details for a specific webhook endpoint.
    def get(self, id: str) -> Webhook:
        return Webhook(**self.execute("get", "/".join(["webhooks", id])))

    # Create a webhook endpoint.
    def create(self, name: str, url: str, secret: str, events: List[str]) -> Webhook:
        params = CreateWebhookInputParams(name, url, secret, events)
        return Webhook(**self.execute("post", "/".join(["webhooks"]), params.to_dict()))

    # Update the webhook endpoint.
    def modify(self, id: str) -> UpdateWebhookRequest:
        return UpdateWebhookRequest(id, self.travelperk)

    # Performs a webhook test call.
    def test(self, id: str):
        return self.travelperk.post("/".join(["webhooks", id, "test"]), [])

    # Deletes a webhook endpoint.
    def delete(self, id: str) -> str:
        return self.travelperk.delete("/".join(["webhooks", id]))
