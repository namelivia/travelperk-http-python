import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.users.users import Users


class TestUsers:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.users = Users(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_users_stub(self, users_page):
        assert users_page.total == 2
        assert users_page.offset == 0
        assert users_page.limit == 10
        assert len(users_page.users) == 2
        assert users_page.users[0].id == "8"
        assert users_page.users[0].user_name == "boss@test.com"
        assert users_page.users[0].name.last_name == "Morrison"
        assert users_page.users[0].name.first_name == "Boss"
        assert users_page.users[0].name.middle_name == ""
        assert users_page.users[0].name.title == "MR"
        assert users_page.users[0].preferred_language == "en"
        assert users_page.users[0].locale == "en-gb"
        assert users_page.users[0].active is True
        assert users_page.users[0].job_title == "Boss"
        assert users_page.users[0].phone_numbers == ["+34 123456789"]
        assert users_page.users[0].emergency_contact.name == "Mrs. Morrison"
        assert users_page.users[0].emergency_contact.phone == "+34 987654321"
        assert users_page.users[1].id == "7"
        assert users_page.users[1].user_name == "manager@test.com"
        assert users_page.users[1].name.last_name == "Roberts"
        assert users_page.users[1].name.first_name == "Manager"
        assert users_page.users[1].name.middle_name == ""
        assert users_page.users[1].name.title == "MRS"
        assert users_page.users[1].preferred_language == "en"
        assert users_page.users[1].locale == "en-gb"
        assert users_page.users[1].active is True
        assert users_page.users[1].job_title == "Office Manager"
        assert users_page.users[1].phone_numbers == []
        assert users_page.users[1].emergency_contact is None

    def test_getting_all_users_with_params_using_query(self):
        self.travelperk.get.return_value = self.get_stub_contents("users.json")
        users_page = self.users.query().set_offset(5).set_limit(10).get()
        self.assert_equals_users_stub(users_page)
        self.travelperk.get.assert_called_once_with("users?offset=5&limit=10")
