from travelperk_http_python.scim.update_user_input_params import UpdateUserInputParams
from travelperk_http_python.scim.name_input_params import NameInputParams


class TestUpdateUserInputParam:
    def test_setting_update_user_input_params_no_name(self):
        input_params = UpdateUserInputParams()
        input_params.set_user_name("New user name").set_active(False)
        assert {
            "userName": "New user name",
            "active": False,
        } == input_params.to_dict()

    def test_setting_update_user_input_params_name(self):
        input_params = UpdateUserInputParams()
        input_params.set_name(NameInputParams("given name", "family name"))
        assert {
            "name": {
                "givenName": "given name",
                "familyName": "family name",
            },
        } == input_params.to_dict()
