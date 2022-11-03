import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.expenses.invoice_profiles import InvoiceProfiles


class TestInvoiceProfiles:
    def setup_method(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.invoice_profiles = InvoiceProfiles(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_stub(self, invoice_profiles_page):
        assert invoice_profiles_page.offset == 0
        assert invoice_profiles_page.limit == 10
        assert invoice_profiles_page.total == 2
        assert len(invoice_profiles_page.profiles) == 2
        assert (
            invoice_profiles_page.profiles[0].id
            == "f2dd1aa3-5601-4725-a520-bd59885bbb16"
        )
        assert invoice_profiles_page.profiles[0].name == "My Company Ltd"
        assert invoice_profiles_page.profiles[0].payment_method_type == "automatic"
        assert invoice_profiles_page.profiles[0].billing_period == "instant"
        assert invoice_profiles_page.profiles[0].currency == "GBP"
        assert (
            invoice_profiles_page.profiles[0].billing_information.legal_name
            == "My Company Ltd"
        )
        assert (
            invoice_profiles_page.profiles[0].billing_information.vat_number
            == "GB123456789"
        )
        assert (
            invoice_profiles_page.profiles[0].billing_information.address_line_1
            == "199 Bishopsgate"
        )
        assert (
            invoice_profiles_page.profiles[0].billing_information.address_line_2
            == "Spitalfields"
        )
        assert invoice_profiles_page.profiles[0].billing_information.city == "London"
        assert (
            invoice_profiles_page.profiles[0].billing_information.postal_code
            == "EC2M 3TY"
        )
        assert (
            invoice_profiles_page.profiles[0].billing_information.country_name
            == "United Kingdom"
        )
        assert (
            invoice_profiles_page.profiles[1].id
            == "8fa66535-5a9a-4a6f-90d8-2986621a706a"
        )
        assert invoice_profiles_page.profiles[1].name == "My Spanish Company SL"
        assert invoice_profiles_page.profiles[1].payment_method_type == "manual"
        assert invoice_profiles_page.profiles[1].billing_period == "monthly"
        assert invoice_profiles_page.profiles[1].currency == "EUR"
        assert (
            invoice_profiles_page.profiles[1].billing_information.legal_name
            == "My Spanish Company SL"
        )
        assert (
            invoice_profiles_page.profiles[1].billing_information.vat_number
            == "ES123456789"
        )
        assert (
            invoice_profiles_page.profiles[1].billing_information.address_line_1
            == "Passeig de Gracia 345"
        )
        assert (
            invoice_profiles_page.profiles[1].billing_information.address_line_2
            == "Planta 14"
        )
        assert invoice_profiles_page.profiles[1].billing_information.city == "Barcelona"
        assert (
            invoice_profiles_page.profiles[1].billing_information.postal_code
            == "080123"
        )
        assert (
            invoice_profiles_page.profiles[1].billing_information.country_name
            == "Spain"
        )

    def test_getting_all_invoice_profiles_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents(
            "invoice_profiles.json"
        )
        invoice_profiles_page = (
            self.invoice_profiles.query().set_limit(20).set_offset(30).get()
        )
        self.travelperk.get.assert_called_once_with("profiles?offset=30&limit=20")
        self.assert_equals_stub(invoice_profiles_page)

    def test_getting_all_invoice_profiles_no_params(self):
        self.travelperk.get.return_value = self.get_stub_contents(
            "invoice_profiles.json"
        )
        invoice_profiles_page = self.invoice_profiles.query().get()
        # TODO: Would it be better without the question mark
        self.travelperk.get.assert_called_once_with("profiles?")
        self.assert_equals_stub(invoice_profiles_page)
