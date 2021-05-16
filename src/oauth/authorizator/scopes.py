from typing import List


class Scopes:
    valid_scopes = [
        "scim:read",
        "scim:write",
        "scim:delete",
        "expenses:read",
    ]

    def __init__(self, scopes: List[str]):
        for scope in scopes:
            if scope not in self.valid_scopes:
                raise Exception(f"The scope {scope} is invalid")
        self.scopes = scopes

    def as_url_param(self) -> str:
        return " ".join(self.scopes)
