from typing import List


class Config:
    def __init__(
        self, client_id: str, client_secret: str, redirect_url: str, code: str = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.code = code

    def get_client_id(self) -> str:
        return self.client_id

    def get_redirect_url(self) -> str:
        return self.redirect_url

    def set_code(self, code: str) -> "Config":
        self.code = code
        return self

    def has_code(self) -> bool:
        return self.code is not None

    def to_dict(self) -> List:
        return {
            "code": self.code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_url,
        }
