from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.scim.discovery import Discovery


class TestDiscovery:
    def setup_method(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.discovery = Discovery(self.travelperk)

    def test_getting_service_provider_config(self):
        self.travelperk.get.return_value = {"data": "serviceProviderConfig"}
        assert {
            "data": "serviceProviderConfig"
        } == self.discovery.service_provider_config()
        self.travelperk.get.assert_called_once_with("scim/ServiceProviderConfig")

    def test_getting_resource_types(self):
        self.travelperk.get.return_value = {"data": "resourceTypes"}
        assert {"data": "resourceTypes"} == self.discovery.resource_types()
        self.travelperk.get.assert_called_once_with("scim/ResourceTypes")

    def test_getting_schemas(self):
        self.travelperk.get.return_value = {"data": "schemas"}
        assert {"data": "schemas"} == self.discovery.schemas()
        self.travelperk.get.assert_called_once_with("scim/Schemas")

    def test_getting_user_schema(self):
        self.travelperk.get.return_value = {"data": "userSchema"}
        assert {"data": "userSchema"} == self.discovery.user_schema()
        self.travelperk.get.assert_called_once_with(
            "scim/Schemas/urn:ietf:params:scim:schemas:core:2.0:User"
        )

    def test_getting_enterprise_user_schema(self):
        self.travelperk.get.return_value = {"data": "enterpriseUserSchema"}
        assert {
            "data": "enterpriseUserSchema"
        } == self.discovery.enterprise_user_schema()
        self.travelperk.get.assert_called_once_with(
            "scim/Schemas/urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
        )
