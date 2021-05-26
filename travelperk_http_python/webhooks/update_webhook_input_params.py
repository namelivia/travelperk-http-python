from typing import List


class UpdateWebhookInputParams:
    def __init__(self):
        self.name = None
        self.url = None
        self.secret = None
        self.enabled = None
        self.events = None

    def set_name(self, name: str) -> "UpdateWebhookInputParams":
        self.name = name
        return self

    def set_enabled(self, enabled: bool) -> "UpdateWebhookInputParams":
        self.enabled = enabled
        return self

    def set_url(self, url: str) -> "UpdateWebhookInputParams":
        self.url = url
        return self

    def set_secret(self, secret: str) -> "UpdateWebhookInputParams":
        self.secret = secret
        return self

    def set_events(self, events: List[str]) -> "UpdateWebhookInputParams":
        self.events = events
        return self

    def to_dict(self) -> dict:
        data = {
            "name": self.name,
            "url": self.url,
            "secret": self.secret,
            "enabled": self.enabled,
            "events": self.events,
        }
        return {k: v for k, v in data.items() if v is not None}
