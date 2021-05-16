import pytest
from src.oauth.authorizator.scopes import Scopes


class TestAuthorizator:
    def test_building_with_invalid_scopes_raises_an_exception(self):
        with pytest.raises(Exception) as e:
            Scopes(["invalid:scope"])
        assert str(e.value) == "The scope invalid:scope is invalid"
