from src.api.travelperk import TravelPerk

# from src.client.client import Client


def build(api_key: str, is_sandbox: bool):
    # client = Client(api_key)
    # return TravelPerk(client, is_sandbox)
    return TravelPerk(is_sandbox)
