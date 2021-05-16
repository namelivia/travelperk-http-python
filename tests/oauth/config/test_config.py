from src.oauth.config.config import Config


class TestConfig:
    @classmethod
    def setup_class(cls):
        cls.config = Config("client-id", "client-secret", "http://redirect.url")

    def test_getting_client_id(self):
        assert self.config.get_client_id() == "client-id"

    def test_getting_redirect_url(self):
        assert self.config.get_redirect_url() == "http://redirect.url"

    def test_checking_and_setting_the_oauth_code(self):
        assert self.config.has_code() is False
        self.config.set_code("auth-code")
        assert self.config.has_code() is True

    def test_checking_the_config_as_a_dict(self):
        assert self.config.to_dict() == {
            "code": "auth-code",
            "client_id": "client-id",
            "client_secret": "client-secret",
            "redirect_uri": "http://redirect.url",
        }
