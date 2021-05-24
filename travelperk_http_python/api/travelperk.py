from typing import List
from .expenses_api import ExpensesAPI
from .scim import SCIM
from .webhooks import Webhooks
from .travelsafe import TravelSafe
from .users import Users
from .trips import Trips
from .cost_centers_api import CostCentersAPI

# from oauth.client.client import Client
from travelperk_http_python.client.client import Client


class TravelPerk:
    BASE_URL = "https://api.travelperk.com/"
    SANDBOX_BASE_URL = "https://sandbox.travelperk.com/"

    def __init__(self, client: Client, is_sandbox: bool):
        """
        $this->scim = new SCIM($this, $mapper);
        $this->webhooks = new WebhooksAPI($this, $mapper);
        $this->travelSafe = new TravelSafeAPI($this, $mapper);
        $this->users = new UsersAPI($this, $mapper);
        $this->trips = new TripsAPI($this, $mapper);
        """
        self.client = client
        self._expenses = ExpensesAPI(self)
        self._scim = SCIM()
        self._webhooks = Webhooks()
        self._travelsafe = TravelSafe()
        self._users = Users()
        self._trips = Trips()
        self._cost_centers = CostCentersAPI(self)
        self.base_url = self.SANDBOX_BASE_URL if is_sandbox else self.BASE_URL

    def get_auth_uri(self, target_link_uri: str) -> str:
        # return self.client.get_auth_uri(target_link_uri)
        return target_link_uri

    def get(self, url: str) -> dict:
        return self.client.get(self.base_url + url)

    def post(self, url: str, params: List[str]) -> str:
        # return self.client.post(
        return self.base_url + url
        # ).get_body().get_contents()

    def patch(self, url: str, params: dict) -> dict:
        return self.client.patch(self.base_url + url, params)

    def put(self, url: str, params: List[str]) -> str:
        # return self.client.put(
        return self.base_url + url
        # ).get_body().get_contents()

    def delete(self, url: str) -> str:
        # return self.client.delete(
        return self.base_url + url
        # ).get_body().get_contents()

    def set_authorization_code(self, authorization_code: str) -> "TravelPerk":
        # self.client.set_authorization_code(authorization_code)
        # return self
        return authorization_code

    def expenses(self) -> ExpensesAPI:
        return self._expenses

    # def scim(self) -> SCIM:
    def scim(self) -> None:
        return self._scim

    # def webhooks(self) -> WebhooksAPI:
    def webhooks(self) -> None:
        return self._webhooks

    # def travelsafe(self) -> TravelSafeAPI:
    def travelsafe(self) -> None:
        return self._travelsafe

    # def users(self) -> UsersAPI:
    def users(self) -> None:
        return self._users

    # def trips(self) -> TripsAPI:
    def trips(self) -> None:
        return self._trips

    def cost_centers(self) -> CostCentersAPI:
        return self._cost_centers
