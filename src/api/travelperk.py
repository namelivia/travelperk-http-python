from typing import List


class TravelPerk:
    BASE_URL = 'https://api.travelperk.com/'
    SANDBOX_BASE_URL = 'https://sandbox.travelperk.com/'

    # def __init__(self, client: Client, is_sandbox: bool):
    def __init__(self, is_sandbox: bool):
        """
        $this->client = $client;
        $this->expenses = new Expenses($this, $mapper);
        $this->scim = new SCIM($this, $mapper);
        $this->webhooks = new WebhooksAPI($this, $mapper);
        $this->travelSafe = new TravelSafeAPI($this, $mapper);
        $this->users = new UsersAPI($this, $mapper);
        $this->trips = new TripsAPI($this, $mapper);
        $this->costCenters = new CostCentersAPI($this, $mapper);
        """
        self._expenses = None
        self._scim = None
        self._webhooks = None
        self._travelsafe = None
        self._users = None
        self._trips = None
        self._cost_centers = None
        self.base_url = self.SANDBOX_BASE_URL if is_sandbox else self.BASE_URL

    def get_auth_uri(self, target_link_uri: str) -> str:
        # return self.client.get_auth_uri(target_link_uri)
        return target_link_uri

    def get(self, url: str) -> str:
        # return self.client.get(
        return self.base_url + url
        # ).get_body().get_contents()

    def post(self, url: str, params: List[str]) -> str:
        # return self.client.post(
        return self.base_url + url
        # ).get_body().get_contents()

    def patch(self, url: str, params: List[str]) -> str:
        # return self.client.patch(
        return self.base_url + url
        # ).get_body().get_contents()

    def put(self, url: str, params: List[str]) -> str:
        # return self.client.put(
        return self.base_url + url
        # ).get_body().get_contents()

    def delete(self, url: str) -> str:
        # return self.client.delete(
        return self.base_url + url
        # ).get_body().get_contents()

    # def setAuthorizationCode(self, authorization_code: str) -> TravelPerk:
    def set_authorization_code(self, authorization_code: str) -> "TravelPerk":
        # self.client.set_authorization_code(authorization_code)
        # return self
        return authorization_code

    # def expenses(self) -> Expenses:
    def expenses(self) -> None:
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

    # def cost_centers(self) -> CostCentersAPI:
    def cost_centers(self) -> None:
        return self._cost_centers
