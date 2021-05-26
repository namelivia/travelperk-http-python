import datetime
from travelperk_http_python.scim.create_user_input_params import CreateUserInputParams
from travelperk_http_python.scim.name_input_params import NameInputParams
from travelperk_http_python.scim.language import Language
from travelperk_http_python.scim.gender import Gender
from travelperk_http_python.scim.emergency_contact import EmergencyContact


class TestCreateUserInputParam:
    def test_setting_create_user_input_params(self):
        input_params = CreateUserInputParams(
            "username", True, NameInputParams("given_name", "family_name")
        )
        assert {
            "userName": "username",
            "name": {
                "givenName": "given_name",
                "familyName": "family_name",
            },
            "active": True,
        } == input_params.to_dict()

    def test_setting_create_user_input_params_with_optional_parameters(self):
        input_params = CreateUserInputParams(
            "username", True, NameInputParams("given_name", "family_name")
        )
        input_params.set_language(Language.SPANISH).set_locale("en-gb").set_title(
            "Manager"
        ).set_external_id("external-id").set_phone_number("787281928").set_gender(
            Gender.MALE
        ).set_date_of_birth(
            datetime.datetime(1990, 3, 23)
        ).set_travel_policy(
            "Travel Policy"
        ).set_invoice_profiles(
            ["Invoice Profile 1", "Invoice Profile 2"]
        ).set_emergency_contact(
            EmergencyContact("Test contact", "679281923")
        ).set_cost_center(
            "Test Cost Center"
        ).set_manager(
            "123"
        )
        assert {
            "userName": "username",
            "name": {
                "givenName": "given_name",
                "familyName": "family_name",
            },
            "active": True,
            "preferredLanguage": "es",
            "locale": "en-gb",
            "title": "Manager",
            "externalId": "external-id",
            "phoneNumbers": [
                {
                    "value": "787281928",
                    "type": "work",
                },
            ],
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User": {
                "gender": "M",
                "dateOfBirth": "1990/03/23",
                "travelPolicy": "Travel Policy",
                "emergencyContact": {
                    "name": "Test contact",
                    "phone": "679281923",
                },
                "invoiceProfiles": [
                    {"value": "Invoice Profile 1"},
                    {"value": "Invoice Profile 2"},
                ],
            },
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "costCenter": "Test Cost Center",
                "manager": {
                    "value": "123",
                },
            },
        } == input_params.to_dict()
