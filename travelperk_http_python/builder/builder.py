from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.client.client import Client


def build(api_key: str, is_sandbox: bool) -> "TravelPerk":
    client = Client(api_key)
    return TravelPerk(client, is_sandbox)
