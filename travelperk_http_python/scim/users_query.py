import humps
from typing import TYPE_CHECKING
from travelperk_http_python.scim.users_input_params import UsersInputParams
from travelperk_python_api_types.scim.users.users import Users

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class UsersQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = UsersInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            response = getattr(self.travelperk, method)(url)
        else:
            response = getattr(self.travelperk, method)(url, params)

        # TODO: This won't go here. Ugly fix!
        for resource in response["Resources"]:
            resource["travelperk_extension"] = resource[
                "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"
            ]
            del resource["urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"]
            resource["enterprise_extension"] = resource[
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ]
            try:
                del resource[
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ]
                resource["enterprise_extension"]["manager"]["ref"] = resource[
                    "enterprise_extension"
                ]["manager"]["$ref"]
                del resource["enterprise_extension"]["manager"]["$ref"]
            except KeyError:
                pass
        # TODO

        return response

    def set_count(self, count: int) -> "UsersQuery":
        self.params.set_count(count)
        return self

    def set_start_index(self, start_index: int) -> "UsersQuery":
        self.params.set_start_index(start_index)
        return self

    def set_filter(self, _filter: str) -> "UsersQuery":
        self.params.set_filter(_filter)
        return self

    def get(self) -> Users:
        return Users(
            **humps.decamelize(
                self.execute(
                    "get",
                    "/".join(["scim", "Users"]) + "?" + self.params.as_url_param(),
                )
            )
        )
