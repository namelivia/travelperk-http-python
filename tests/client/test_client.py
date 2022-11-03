import pytest
import json
from mock import patch
from travelperk_http_python.client.client import Client
from requests.models import Response
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)


class TestClient:
    def setup_method(self):
        self.client = Client("some_api_key")

    @patch("requests.get")
    def test_raising_exceptions_for_4xx_response(self, m_get):
        response = Response()
        response.status_code = 409
        response._content = str.encode(
            json.dumps("this_is_some_error_explanation_that_needs_to_be_long")
        )
        m_get.return_value = response
        with pytest.raises(TravelPerkHttpException) as e:
            self.client.get("some_url")
            assert e.message == "this_is_some_error_explanation_that_needs_to_be_long"

    @patch("requests.get")
    def test_raising_exceptions_for_5xx_response(self, m_get):
        response = Response()
        response.status_code = 503
        response._content = str.encode(
            json.dumps("this_is_some_error_explanation_that_needs_to_be_long")
        )
        m_get.return_value = response
        with pytest.raises(TravelPerkHttpException) as e:
            self.client.get("some_url")
            assert e.message == "this_is_some_error_explanation_that_needs_to_be_long"

    @patch("requests.get")
    def test_get_content_for_2xx_non_json_response(self, m_get):
        response = Response()
        response.status_code = 200
        response._content = str.encode(
            json.dumps("this_is_some_content_string_that_needs_to_be_long")
        )
        m_get.return_value = response
        response = self.client.get("some_url")
        assert response == '"this_is_some_content_string_that_needs_to_be_long"'

    @patch("requests.get")
    def test_decoding_content_for_2xx_json_response(self, m_get):
        response = Response()
        response.status_code = 200
        response.headers = {"Content-Type": "application/json"}
        response._content = str.encode(
            json.dumps({"data": "this_is_some_content_string_that_needs_to_be_long"})
        )
        m_get.return_value = response
        response = self.client.get("some_url")
        assert response["data"] == "this_is_some_content_string_that_needs_to_be_long"

    @patch("requests.get")
    def test_getting_content_for_empty_2xx_json_response(self, m_get):
        response = Response()
        response.status_code = 200
        response.headers = {"Content-Type": "application/json"}
        response._content = str.encode("")
        m_get.return_value = response
        response = self.client.get("some_url")
        assert response == ""
