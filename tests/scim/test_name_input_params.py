from travelperk_http_python.scim.name_input_params import NameInputParams


class TestNameInputParams:
    def test_setting_just_mandatory_fields(self):
        assert {
            "givenName": "Given Name",
            "familyName": "Family Name",
        } == NameInputParams("Given Name", "Family Name").to_dict()

    def test_setting_all_fields(self):
        assert {
            "givenName": "Given Name",
            "familyName": "Family Name",
            "honorificPrefix": "Honorific Prefix",
            "middleName": "Middle Name",
        } == NameInputParams("Given Name", "Family Name").set_middle_name(
            "Middle Name"
        ).set_honorific_prefix(
            "Honorific Prefix"
        ).to_dict()
