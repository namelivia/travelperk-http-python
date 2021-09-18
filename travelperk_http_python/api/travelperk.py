from typing import List
from .expenses_api import ExpensesAPI
from .scim_api import SCIMAPI
from .webhooks_api import WebhooksAPI
from .travelsafe_api import TravelSafeAPI
from .users_api import UsersAPI
from .trips_api import TripsAPI
from .cost_centers_api import CostCentersAPI

# from oauth.client.client import Client
from travelperk_http_python.client.client import Client


class TravelPerk:
    BASE_URL = "https://api.travelperk.com/"
    SANDBOX_BASE_URL = "https://sandbox.travelperk.com/"

    def __init__(self, client: Client, is_sandbox: bool):
        self.client = client
        self._expenses = ExpensesAPI(self)
        self._scim = SCIMAPI(self)
        self._webhooks = WebhooksAPI(self)
        self._travelsafe = TravelSafeAPI(self)
        self._users = UsersAPI(self)
        self._trips = TripsAPI(self)
        self._cost_centers = CostCentersAPI(self)
        self.base_url = self.SANDBOX_BASE_URL if is_sandbox else self.BASE_URL

    def get_auth_uri(self, target_link_uri: str) -> str:
        # return self.client.get_auth_uri(target_link_uri)
        return target_link_uri

    def get(self, url: str) -> dict:
        return self.client.get(self.base_url + url)

    def post(self, url: str, params: List[str]) -> str:
        return self.client.post(self.base_url + url, params)

    def patch(self, url: str, params: dict) -> dict:
        return self.client.patch(self.base_url + url, params)

    def put(self, url: str, params: List[str]) -> str:
        return self.client.put(self.base_url + url, params)

    def delete(self, url: str) -> str:
        return self.client.delete(self.base_url + url)

    def set_authorization_code(self, authorization_code: str) -> "TravelPerk":
        # self.client.set_authorization_code(authorization_code)
        # return self
        return authorization_code

    def expenses(self) -> ExpensesAPI:
        return self._expenses

    def scim(self) -> SCIMAPI:
        return self._scim

    def webhooks(self) -> WebhooksAPI:
        return self._webhooks

    def travelsafe(self) -> TravelSafeAPI:
        return self._travelsafe

    def users(self) -> UsersAPI:
        return self._users

    def trips(self) -> TripsAPI:
        return self._trips

    def cost_centers(self) -> CostCentersAPI:
        return self._cost_centers
