import urllib
from travelperk_http_python.scim.users_input_params import UsersInputParams


class TestUsersInputParam:
    def test_setting_users_all_input_params(self):
        input_params = UsersInputParams()
        input_params.set_count(4).set_start_index(3).set_filter("filter")
        assert "count=4&startIndex=3&filter=filter" == urllib.parse.unquote(
            input_params.as_url_param()
        )

    def test_setting_users_some_input_params(self):
        input_params = UsersInputParams()
        input_params.set_start_index(3)
        assert "startIndex=3" == urllib.parse.unquote(input_params.as_url_param())

    def test_setting_users_no_input_params(self):
        input_params = UsersInputParams()
        assert urllib.parse.unquote(input_params.as_url_param()) == ""
