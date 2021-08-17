from requests_oauthlib import OAuth2Session
from typing import List
from travelperk_http_python.oauth.constants.constants import TOKEN_URL, AUTHORIZE_URL


class Client:
    def __init__(
        self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]
    ):
        self.client_secret = client_secret
        self.oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)
        self.headers = {
            "Api-Version": "1",
        }
        self.is_authorized = False

    def check_authorized(self) -> None:
        if not self.is_authorized:
            raise Exception("Unauthorized")  # TODO: Custom exception

    def get_auth_uri(self, target_link_uri: str) -> str:
        authorization_url, state = self.oauth.authorization_url(
            AUTHORIZE_URL + target_link_uri,
            # TODO: This should be more sofisticate to avoid vulnerabilities.
            # https://github.com/namelivia/travelperk-http-php/issues/21
            # base64 encoded info could be sent to have url, method and also a nonce.
            # More info here: https://tools.ietf.org/id/draft-bradley-oauth-jwt-encoded-state-08.html
            state=target_link_uri,
        )
        return authorization_url

    def set_authorization_code(self, code: str) -> "Client":
        self.authorization_code = code
        self.is_authorized = True
        return self

    # This is not on the PHP version. When could I do it?
    # Maybe when setting the authorization code?
    # Maybe before each request if the authorization code is present?
    def set_token(self) -> "Client":
        self.token = self.oauth.fetch_token(
            TOKEN_URL,
            authorization_response=self.authorization_code,
            client_secret=self.client_secret,
        )
        return self

    # Checks if authorized before every HTTP method
    def get(self, uri: str) -> dict:
        self.check_authorized()
        return self.oauth.get(uri, headers=self.headers).json()

    def delete(self, uri: str) -> dict:
        self.check_authorized()
        return self.oauth.delete(uri, headers=self.headers)

    def post(self, uri: str, data: dict) -> dict:
        self.check_authorized()
        return self.oauth.post(uri, json=data, headers=self.headers).json()

    def post_raw(self, uri: str, data: dict):
        self.check_authorized()
        return self.oauth.post(uri, json=data, headers=self.headers)

    def put(self, uri: str, data: dict) -> dict:
        self.check_authorized()
        return self.oauth.put(uri, json=data, headers=self.headers).json()

    def patch(self, uri: str, data: dict) -> dict:
        self.check_authorized()
        return self.oauth.patch(uri, json=data, headers=self.headers).json()
