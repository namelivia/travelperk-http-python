import requests


class Client:
    def __init__(self, api_key: str):
        self.headers = {
            "Api-Version": "1",
            "Authorization": "ApiKey " + api_key,
        }

    def set_authorization_code(self, authorization_code: str) -> str:
        raise NotImplementedError(
            "No authorization code needed for simple api key authentication"
        )

    def get_auth_uri(self, target_link_uri: str) -> str:
        raise NotImplementedError(
            "No authorization URI for simple api key authentication"
        )

    def get(self, uri: str) -> dict:
        return requests.get(uri, headers=self.headers).json()

    def delete(self, uri: str) -> dict:
        return requests.delete(uri).json()

    def patch(self, uri: str, data: dict) -> dict:
        return requests.patch(uri, data=data, headers=self.headers).json()

    def post(self, uri: str, data: dict) -> dict:
        return requests.post(uri, data=data, headers=self.headers).json()

    def put(self, uri: str, data: dict) -> dict:
        return requests.put(uri, data=data, headers=self.headers).json()
