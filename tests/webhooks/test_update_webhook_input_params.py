from travelperk_http_python.webhooks.update_webhook_input_params import (
    UpdateWebhookInputParams,
)


class TestUpdateWebhookInputParams:
    def test_setting_update_webhook_input_params(self):
        input_params = UpdateWebhookInputParams()
        input_params.set_enabled(False).set_name("New name").set_url(
            "New url"
        ).set_secret("New secret").set_events(["New event"])
        assert {
            "name": "New name",
            "enabled": False,
            "url": "New url",
            "secret": "New secret",
            "events": ["New event"],
        } == input_params.to_dict()
