from urllib.parse import urlencode
from typing import List
from .scopes import Scopes
from travelperk_http_python.oauth.config.config import Config
from travelperk_http_python.oauth.constants.constants import AUTHORIZE_URL


class Authorizator:
    def __init__(
        self,
        config: Config,
        # TODO: Token persistence
        scopes: List[str],
    ):
        self.config = config
        self.scopes = Scopes(scopes)

    def get_auth_uri(self, target_link_uri: str) -> str:
        return (
            AUTHORIZE_URL
            + "?"
            + urlencode(
                {
                    "client_id": self.config.get_client_id(),
                    "redirect_uri": self.config.get_redirect_url(),
                    "scope": self.scopes.as_url_param(),
                    "response_type": "code",
                    # TODO: This should be more sofisticate to avoid vulnerabilities.
                    # https://github.com/namelivia/travelperk-http-php/issues/21
                    # base64 encoded info could be sent to have url, method and also a nonce.
                    # More info here: https://tools.ietf.org/id/draft-bradley-oauth-jwt-encoded-state-08.html
                    "state": target_link_uri,
                }
            )
        )

    def set_authorization_code(self, code: str) -> "Authorizator":
        self.config.set_code(code)
        return self

    def is_authorized(self) -> bool:
        # return self.token_persistence->has_token() or self.config.has_code()
        return self.config.has_code()
