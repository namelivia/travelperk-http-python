import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.webhooks.webhooks import Webhooks
from travelperk_http_python.webhooks.update_webhook_input_params import (
    UpdateWebhookInputParams,
)


class TestWebhooks:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.webhooks = Webhooks(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def test_getting_all_events(self):
        self.travelperk.get.return_value = self.get_stub_contents("events.json")
        events = self.webhooks.events()
        self.travelperk.get.assert_called_once_with("webhooks/events")
        assert len(events) == 2
        assert events[0].name == "invoice.issued"
        assert events[0].topic == "invoices"
        assert events[1].name == "invoiceline.created"
        assert events[0].topic == "invoices"

    def test_getting_all_webhooks(self):
        self.travelperk.get.return_value = self.get_stub_contents("webhooks.json")
        webhooks = self.webhooks.all()
        self.travelperk.get.assert_called_once_with("webhooks")
        assert len(webhooks.webhooks) == 1
        assert webhooks.webhooks[0].id == "b42820bb-24c9-48da-bded-487681e9c851"
        assert webhooks.webhooks[0].name == "invoice webhook"
        assert webhooks.webhooks[0].url == "https://mycompany/tkwebhook"
        assert webhooks.webhooks[0].secret == "some secret"
        assert webhooks.webhooks[0].enabled is True
        assert len(webhooks.webhooks[0].events) == 2
        assert webhooks.webhooks[0].events[0] == "invoice.issued"
        assert webhooks.webhooks[0].events[1] == "invoiceline.created"
        assert webhooks.webhooks[0].successfully_sent == 2
        assert webhooks.webhooks[0].failed_sent == 0
        assert webhooks.webhooks[0].error_rate == 0.0

    def test_getting_a_webhook_detail(self):
        self.travelperk.get.return_value = self.get_stub_contents("webhook.json")
        webhook_id = "1a"
        webhook = self.webhooks.get(webhook_id)
        self.travelperk.get.assert_called_once_with("webhooks/1a")
        assert webhook.id == "b42820bb-24c9-48da-bded-487681e9c851"
        assert webhook.name == "invoice webhook"
        assert webhook.url == "https://mycompany.com/tk_webhook"
        assert webhook.secret == "some secret"
        assert webhook.enabled is True
        assert len(webhook.events) == 2
        assert webhook.events[0] == "invoice.issued"
        assert webhook.events[1] == "invoiceline.created"
        assert webhook.successfully_sent == 2
        assert webhook.failed_sent == 0
        assert webhook.error_rate == 0.0

    def test_testing_a_webhook(self):
        self.travelperk.post.return_value = "webhookTestResponse"
        webhook_id = "1a"
        assert "webhookTestResponse" == self.webhooks.test(webhook_id)
        self.travelperk.post.assert_called_once_with("webhooks/1a/test", [])

    def test_deleting_a_webhook(self):
        self.travelperk.delete.return_value = "webhookDeleted"
        webhook_id = "1a"
        assert "webhookDeleted" == self.webhooks.delete(webhook_id)
        self.travelperk.delete.assert_called_once_with("webhooks/1a")

    def test_creating_a_webhook(self):
        self.travelperk.post.return_value = self.get_stub_contents("webhook.json")
        new_webhook = self.webhooks.create(
            "name",
            "url",
            "secret",
            ["event1", "event2"],
        )
        self.travelperk.post.assert_called_once_with(
            "webhooks",
            {
                "name": "name",
                "url": "url",
                "secret": "secret",
                "events": ["event1", "event2"],
            },
        )
        assert new_webhook.id == "b42820bb-24c9-48da-bded-487681e9c851"
        assert new_webhook.name == "invoice webhook"
        assert new_webhook.url == "https://mycompany.com/tk_webhook"
        assert new_webhook.secret == "some secret"
        assert new_webhook.enabled is True
        assert len(new_webhook.events) == 2
        assert new_webhook.events[0] == "invoice.issued"
        assert new_webhook.events[1] == "invoiceline.created"
        assert new_webhook.successfully_sent == 2
        assert new_webhook.failed_sent == 0
        assert new_webhook.error_rate == 0.0

    def test_modifying_a_webhook(self):
        webhook_id = "1a"
        self.travelperk.patch.return_value = self.get_stub_contents("webhook.json")
        updated_webhook = (
            self.webhooks.modify(webhook_id)
            .set_name("newName")
            .set_enabled(False)
            .save()
        )
        self.travelperk.patch.assert_called_once_with(
            "webhooks/1a",
            {
                "name": "newName",
                "enabled": False,
            },
        )
        assert updated_webhook.id == "b42820bb-24c9-48da-bded-487681e9c851"
        assert updated_webhook.name == "invoice webhook"
        assert updated_webhook.url == "https://mycompany.com/tk_webhook"
        assert updated_webhook.secret == "some secret"
        assert updated_webhook.enabled is True
        assert len(updated_webhook.events) == 2
        assert updated_webhook.events[0] == "invoice.issued"
        assert updated_webhook.events[1] == "invoiceline.created"
        assert updated_webhook.successfully_sent == 2
        assert updated_webhook.failed_sent == 0
        assert updated_webhook.error_rate == 0.0
