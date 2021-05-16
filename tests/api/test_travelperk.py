from src.api.travelperk import TravelPerk
from src.api.expenses import Expenses
from src.api.scim import SCIM
from src.api.webhooks import Webhooks
from src.api.travelsafe import TravelSafe
from src.api.users import Users
from src.api.trips import Trips
from src.api.cost_centers_api import CostCentersAPI


class TestTravelPerk:
    def setup(self):
        self.travelperk = TravelPerk(False)

    def test_making_a_get_call(self):
        assert (
            self.travelperk.get("sampleurl") == "https://api.travelperk.com/sampleurl"
        )

    def test_making_a_post_call(self):
        assert (
            self.travelperk.post("sampleurl", [])
            == "https://api.travelperk.com/sampleurl"
        )

    def test_making_a_put_call(self):
        assert (
            self.travelperk.put("sampleurl", [])
            == "https://api.travelperk.com/sampleurl"
        )

    def test_making_a_patch_call(self):
        assert (
            self.travelperk.patch("sampleurl", [])
            == "https://api.travelperk.com/sampleurl"
        )

    def test_making_a_delete_call(self):
        assert (
            self.travelperk.delete("sampleurl")
            == "https://api.travelperk.com/sampleurl"
        )

    def test_getting_an_expenses_instance(self):
        assert type(self.travelperk.expenses()) is Expenses

    def test_getting_a_scim_instance(self):
        assert type(self.travelperk.scim()) is SCIM

    def test_getting_a_webhooks_instance(self):
        assert type(self.travelperk.webhooks()) is Webhooks

    def test_getting_a_travelsafe_instance(self):
        assert type(self.travelperk.travelsafe()) is TravelSafe

    def test_getting_a_users_instance(self):
        assert type(self.travelperk.users()) is Users

    def test_getting_a_trips_instance(self):
        assert type(self.travelperk.trips()) is Trips

    def test_getting_a_cost_centers_instance(self):
        assert type(self.travelperk.cost_centers()) is CostCentersAPI

    def test_querying_the_sandbox_environment(self):
        travelperk = TravelPerk(True)
        assert travelperk.get("sampleurl") == "https://sandbox.travelperk.com/sampleurl"

    def test_getting_auth_uri(self):
        assert self.travelperk.get_auth_uri("target/link/uri") == "target/link/uri"

    def test_setting_auth_code(self):
        assert self.travelperk.set_authorization_code("auth-code") == "auth-code"
