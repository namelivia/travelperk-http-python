from travelperk_http_python.webhooks.create_webhook_input_params import (
    CreateWebhookInputParams,
)


class TestCreateWebhookInputParams:
    def test_setting_create_webhook_input_params(self):
        input_params = CreateWebhookInputParams(
            "webhook", "https://test.com", "SECRET_KEY", []
        )
        assert {
            "name": "webhook",
            "url": "https://test.com",
            "secret": "SECRET_KEY",
            "events": [],
        } == input_params.to_dict()
