import requests
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)


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

    def _get_content(self, response):
        if response.status_code // 100 != 2:
            raise TravelPerkHttpException(response.text)
        if (
            "Content-Type" in response.headers
            and "json" in response.headers["Content-Type"]
        ):
            return response.json()
        return response.text

    def get(self, uri: str) -> dict:
        return self._get_content(requests.get(uri, headers=self.headers))

    def delete(self, uri: str) -> dict:
        return self._get_content(requests.delete(uri, headers=self.headers))

    def patch(self, uri: str, data: dict) -> dict:
        return self._get_content(requests.patch(uri, json=data, headers=self.headers))

    def post(self, uri: str, data: dict) -> dict:
        return self._get_content(requests.post(uri, json=data, headers=self.headers))

    def put(self, uri: str, data: dict) -> dict:
        return self._get_content(requests.put(uri, json=data, headers=self.headers))
