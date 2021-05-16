import pytest
from mock import Mock
from src.oauth.authorizator.authorizator import Authorizator
from src.oauth.config.config import Config


class TestAuthorizator:
    def setup(self):
        self.config = Mock(spec=Config)
        # TODO: Token persistence
        self.scopes = ["expenses:read"]
        self.authorizator = Authorizator(self.config, self.scopes)

    def test_checking_authorized_no_code_on_config(self):
        self.config.has_code.return_value = False
        assert self.authorizator.is_authorized() is False
        self.config.has_code.assert_called_once_with()

    def test_checking_authorized_code_on_config(self):
        self.config.has_code.return_value = True
        assert self.authorizator.is_authorized() is True
        self.config.has_code.assert_called_once_with()

    def test_setting_the_authorization_code(self):
        assert self.authorizator.set_authorization_code("auth-code")
        self.config.set_code.assert_called_once_with("auth-code")

    def test_getting_the_auth_uri(self):
        self.config.get_client_id.return_value = "client-id"
        self.config.get_redirect_url.return_value = "http://redirect.url"
        assert (
            self.authorizator.get_auth_uri("/target/link")
            == "https://app.travelperk.com/oauth2/authorize/?client_id=client-id&redirect_uri=http%3A%2F%2Fredirect.url&scope=expenses%3Aread&response_type=code&state=%2Ftarget%2Flink"
        )
        self.config.get_client_id.assert_called_once_with()
        self.config.get_redirect_url.assert_called_once_with()

    def test_building_with_invalid_scopes_rise_exception(self):
        with pytest.raises(Exception) as e:
            Authorizator(
                self.config,
                # self.token_persistence,
                self.scopes + ["invalid:scope"],
            )
        assert str(e.value) == "The scope invalid:scope is invalid"
