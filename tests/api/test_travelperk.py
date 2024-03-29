from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.api.expenses_api import ExpensesAPI
from travelperk_http_python.api.scim_api import SCIMAPI
from travelperk_http_python.api.webhooks_api import WebhooksAPI
from travelperk_http_python.api.travelsafe_api import TravelSafeAPI
from travelperk_http_python.api.greenperk_api import GreenPerkAPI
from travelperk_http_python.api.users_api import UsersAPI
from travelperk_http_python.api.trips_api import TripsAPI
from travelperk_http_python.api.cost_centers_api import CostCentersAPI
from travelperk_http_python.client.client import Client


class TestTravelPerk:
    def setup_method(self):
        self.client = Mock(spec=Client)
        self.travelperk = TravelPerk(self.client, False)

    def test_making_a_get_call(self):
        response = {"data": "test_data"}
        self.client.get.return_value = response
        result = self.travelperk.get("sampleurl")
        self.client.get.assert_called_once_with("https://api.travelperk.com/sampleurl")
        assert result == response

    def test_making_a_post_call(self):
        response = {"data": "test_data"}
        self.client.post.return_value = response
        result = self.travelperk.post("sampleurl", {"data": "test"})
        self.client.post.assert_called_once_with(
            "https://api.travelperk.com/sampleurl", {"data": "test"}
        )
        assert result == response

    def test_making_a_put_call(self):
        response = {"data": "test_data"}
        self.client.put.return_value = response
        result = self.travelperk.put("sampleurl", {"data": "test"})
        self.client.put.assert_called_once_with(
            "https://api.travelperk.com/sampleurl", {"data": "test"}
        )
        assert result == response

    def test_making_a_patch_call(self):
        response = {"data": "test_data"}
        self.client.patch.return_value = response
        result = self.travelperk.patch("sampleurl", {"data": "test"})
        self.client.patch.assert_called_once_with(
            "https://api.travelperk.com/sampleurl", {"data": "test"}
        )
        assert result == response

    def test_making_a_delete_call(self):
        self.travelperk.delete("sampleurl")
        self.client.delete.assert_called_once_with(
            "https://api.travelperk.com/sampleurl"
        )

    def test_getting_an_expenses_instance(self):
        assert type(self.travelperk.expenses()) is ExpensesAPI

    def test_getting_a_scim_instance(self):
        assert type(self.travelperk.scim()) is SCIMAPI

    def test_getting_a_webhooks_instance(self):
        assert type(self.travelperk.webhooks()) is WebhooksAPI

    def test_getting_a_travelsafe_instance(self):
        assert type(self.travelperk.travelsafe()) is TravelSafeAPI

    def test_getting_a_greenperk_instance(self):
        assert type(self.travelperk.greenperk()) is GreenPerkAPI

    def test_getting_a_users_instance(self):
        assert type(self.travelperk.users()) is UsersAPI

    def test_getting_a_trips_instance(self):
        assert type(self.travelperk.trips()) is TripsAPI

    def test_getting_a_cost_centers_instance(self):
        assert type(self.travelperk.cost_centers()) is CostCentersAPI

    def test_querying_the_sandbox_environment(self):
        travelperk = TravelPerk(self.client, True)
        travelperk.get("sampleurl")
        self.client.get.assert_called_once_with(
            "https://api.sandbox-travelperk.com/sampleurl"
        )

    def test_getting_auth_uri(self):
        assert self.travelperk.get_auth_uri("target/link/uri") == "target/link/uri"

    def test_setting_auth_code(self):
        assert self.travelperk.set_authorization_code("auth-code") == "auth-code"
