from typing import List
from .update_webhook_input_params import UpdateWebhookInputParams


class CreateWebhookInputParams:
    def __init__(self, name: str, url: str, secret: str, events: List[str]):
        self.params = (
            UpdateWebhookInputParams()
            .set_name(name)
            .set_url(url)
            .set_secret(secret)
            .set_events(events)
        )

    def to_dict(self) -> dict:
        return self.params.to_dict()
