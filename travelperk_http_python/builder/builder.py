from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.client.client import Client
from travelperk_http_python.oauth.client.client import Client as OAuth2Client
from typing import List


def build(api_key: str, is_sandbox: bool) -> "TravelPerk":
    client = Client(api_key)
    return TravelPerk(client, is_sandbox)


def build_oauth2(
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    scopes: List[str],
    is_sandbox: bool,
) -> "TravelPerk":
    client = OAuth2Client(
        client_id,
        client_secret,
        redirect_uri,
        scopes,
    )
    return TravelPerk(client, is_sandbox)
