from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class Discovery:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # Returns TravelPerk's configuration details for our SCIM API,
    # including which operations are supported.
    def service_provider_config(self) -> dict:
        return self.travelperk.get("/".join(["scim", "ServiceProviderConfig"]))

    # Returns all available resources types for our SCIM API.
    def resource_types(self) -> dict:
        return self.travelperk.get("/".join(["scim", "ResourceTypes"]))

    # List all schemas and their attributes.
    def schemas(self) -> dict:
        return self.travelperk.get("/".join(["scim", "Schemas"]))

    # List all attributes for the User schema.
    def user_schema(self) -> dict:
        return self.travelperk.get(
            "/".join(["scim", "Schemas", "urn:ietf:params:scim:schemas:core:2.0:User"])
        )

    # List all attributes for the Enterprise User schema.
    def enterprise_user_schema(self) -> dict:
        return self.travelperk.get(
            "/".join(
                [
                    "scim",
                    "Schemas",
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                ]
            )
        )
