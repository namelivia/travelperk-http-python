import pytest
from travelperk_http_python.oauth.client.client import Client


class TestClient:
    def setup(self):
        self.client = Client(
            "some client id",
            "some client secret",
            "some.redirect.uri",
            [
                "scope 1",
                "scope 2",
                "scope 3",
            ],
        )

    def test_checking_and_setting_authorization_code(self):
        with pytest.raises(Exception) as e:
            self.client.check_authorized()
            assert str(e) == "Unauthorized"
        self.client.set_authorization_code("some authorization code")
        assert self.client.check_authorized() is None

    def test_getting_the_authentication_uri(self):
        assert (
            self.client.get_auth_uri("some/path")
            == "https://app.travelperk.com/oauth2/authorize/some/path?response_type=code&client_id=some+client+id&redirect_uri=some.redirect.uri&scope=scope+1+scope+2+scope+3&state=some%2Fpath"
        )
