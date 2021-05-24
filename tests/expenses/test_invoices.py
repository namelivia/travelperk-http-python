import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.expenses.invoices import Invoices
from travelperk_http_python.expenses.invoice_lines_input_params import (
    InvoiceLinesInputParams,
)
from travelperk_http_python.expenses.invoices_input_params import InvoicesInputParams


class TestInvoices:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.invoices = Invoices(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_stub(self, invoice_lines_page):
        assert invoice_lines_page.total == 1
        assert invoice_lines_page.offset == 0
        assert invoice_lines_page.limit == 10
        assert len(invoice_lines_page.invoice_lines) == 1
        assert invoice_lines_page.invoice_lines[0].expense_date == "2020-02-13"
        assert (
            invoice_lines_page.invoice_lines[0].description
            == "FLIGHT for Trip ID 1687664"
        )
        assert invoice_lines_page.invoice_lines[0].quantity == 1
        assert invoice_lines_page.invoice_lines[0].unit_price == "20.00000000"
        assert invoice_lines_page.invoice_lines[0].non_taxable_unit_price == "0E-8"
        assert invoice_lines_page.invoice_lines[0].tax_percentage == "0E-8"
        assert invoice_lines_page.invoice_lines[0].tax_amount == "0E-8"
        assert invoice_lines_page.invoice_lines[0].tax_regime == "STAR"
        assert invoice_lines_page.invoice_lines[0].total_amount == "20.00000000"
        assert (
            invoice_lines_page.invoice_lines[0].invoice_serial_number == "INV-01-190111"
        )
        assert (
            invoice_lines_page.invoice_lines[0].profile_id
            == "09d649d1-35fa-4d9f-b688-046d5790afd2"
        )
        assert invoice_lines_page.invoice_lines[0].profile_name == "My Company Ltd"
        assert invoice_lines_page.invoice_lines[0].invoice_mode == "reseller"
        assert invoice_lines_page.invoice_lines[0].invoice_status == "paid"
        assert invoice_lines_page.invoice_lines[0].issuing_date == "2020-02-13"
        assert invoice_lines_page.invoice_lines[0].due_date == "2020-02-13"
        assert invoice_lines_page.invoice_lines[0].currency == "EUR"
        assert invoice_lines_page.invoice_lines[0].metadata.trip_id == 1687664
        assert (
            invoice_lines_page.invoice_lines[0].metadata.trip_name
            == "Meeting with German company GmbH"
        )
        assert invoice_lines_page.invoice_lines[0].metadata.service == "flight"
        assert len(invoice_lines_page.invoice_lines[0].metadata.travelers) == 1
        assert (
            invoice_lines_page.invoice_lines[0].metadata.travelers[0].name == "John Doe"
        )
        assert (
            invoice_lines_page.invoice_lines[0].metadata.travelers[0].email
            == "john.doe@mycompany.com"
        )
        assert (
            invoice_lines_page.invoice_lines[0].metadata.travelers[0].external_id
            == "ASD123"
        )
        assert invoice_lines_page.invoice_lines[0].metadata.start_date == "2020-03-27"
        assert invoice_lines_page.invoice_lines[0].metadata.end_date == "2020-04-05"
        assert (
            invoice_lines_page.invoice_lines[0].metadata.cost_center == "DACH Accounts"
        )
        assert invoice_lines_page.invoice_lines[0].metadata.labels == [
            "Sales trips",
            "Special",
        ]
        assert invoice_lines_page.invoice_lines[0].metadata.vendor.code == "LH"
        assert invoice_lines_page.invoice_lines[0].metadata.vendor.name == "Lufthansa"
        assert invoice_lines_page.invoice_lines[0].metadata.out_of_policy is False
        assert len(invoice_lines_page.invoice_lines[0].metadata.approvers) == 1
        assert (
            invoice_lines_page.invoice_lines[0].metadata.approvers[0].name
            == "Jake Bolt"
        )
        assert (
            invoice_lines_page.invoice_lines[0].metadata.approvers[0].email
            == "jake.bolt@mycompany.com"
        )
        assert (
            invoice_lines_page.invoice_lines[0].metadata.approvers[0].external_id
            == "ASD124"
        )
        assert invoice_lines_page.invoice_lines[0].metadata.booker.name == "Marien Lint"
        assert (
            invoice_lines_page.invoice_lines[0].metadata.booker.email
            == "marien.lint@mycompany.com"
        )
        assert (
            invoice_lines_page.invoice_lines[0].metadata.booker.external_id == "ASD124"
        )

    def assert_equals_invoices_stub(self, invoices_page):
        assert invoices_page.total == 1
        assert invoices_page.offset == 0
        assert invoices_page.limit == 10
        assert len(invoices_page.invoices) == 1
        assert invoices_page.invoices[0].serial_number == "INV-01-987654"
        assert (
            invoices_page.invoices[0].profile_id
            == "edb6322b-8e11-48e9-8d6f-6402e445e50d"
        )
        assert invoices_page.invoices[0].profile_name == "My Company Ltd"
        assert (
            invoices_page.invoices[0].billing_information.legal_name == "My Company Ltd"
        )
        assert invoices_page.invoices[0].billing_information.vat_number == "GB123456789"
        assert (
            invoices_page.invoices[0].billing_information.address_line_1
            == "199 Bishopsgate"
        )
        assert (
            invoices_page.invoices[0].billing_information.address_line_2
            == "Spitalfields"
        )
        assert invoices_page.invoices[0].billing_information.city == "London"
        assert invoices_page.invoices[0].billing_information.postal_code == "EC2M 3TY"
        assert (
            invoices_page.invoices[0].billing_information.country_name
            == "United Kingdom"
        )
        assert invoices_page.invoices[0].mode == "reseller"
        assert invoices_page.invoices[0].status == "paid"
        assert invoices_page.invoices[0].issuing_date == "2020-03-31"
        assert invoices_page.invoices[0].billing_period == "monthly"
        assert invoices_page.invoices[0].from_date == "2020-03-01"
        assert invoices_page.invoices[0].to_date == "2020-03-31"
        assert invoices_page.invoices[0].due_date == "2020-04-15"
        assert invoices_page.invoices[0].currency == "EUR"
        assert invoices_page.invoices[0].total == "13579.24"
        assert invoices_page.invoices[0].lines.total == "15"
        # TODO: This is missing
        assert invoices_page.invoices[0].lines.data == []
        assert (
            invoices_page.invoices[0].lines.next
            == "/invoices/lines?serial_number=INV-01-987654&offset=10"
        )
        assert len(invoices_page.invoices[0].taxes_summary) == 2
        assert invoices_page.invoices[0].taxes_summary[0].tax_regime == "STAR"
        assert invoices_page.invoices[0].taxes_summary[0].subtotal == "6543.21"
        assert invoices_page.invoices[0].taxes_summary[0].tax_percentage == "0.00"
        assert invoices_page.invoices[0].taxes_summary[0].tax_amount == "0.00"
        assert invoices_page.invoices[0].taxes_summary[0].total == "6543.21"
        assert invoices_page.invoices[0].taxes_summary[1].tax_regime == "G-VAT-R"
        assert invoices_page.invoices[0].taxes_summary[1].subtotal == "5912.63"
        assert invoices_page.invoices[0].taxes_summary[1].tax_percentage == "19.00"
        assert invoices_page.invoices[0].taxes_summary[1].tax_amount == "1123.40"
        assert invoices_page.invoices[0].taxes_summary[1].total == "7036.03"
        assert (
            invoices_page.invoices[0].reference
            == "My Company Ltd - SEPA - Monthly 2020-03"
        )
        assert invoices_page.invoices[0].travelperk_bank_account.bank_name == "La Caixa"
        assert (
            invoices_page.invoices[0].travelperk_bank_account.account_number
            == "ES01 2345 6789 1098 7654 3210"
        )
        assert invoices_page.invoices[0].travelperk_bank_account.bic == "CAIX ES BB XXX"
        assert (
            invoices_page.invoices[0].travelperk_bank_account.reference
            == "INV-01-987654"
        )
        assert (
            invoices_page.invoices[0].pdf
            == "https://api.travelperk.com/invoices/INV-01-987654/pdf"
        )

    def test_getting_all_invoices_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoices.json")
        invoices = self.invoices.query().set_offset(5).set_limit(10).get()
        self.travelperk.get.assert_called_once_with("invoices?offset=5&limit=10")
        self.assert_equals_invoices_stub(invoices)

    def test_getting_all_invoices_no_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoices.json")
        invoices = self.invoices.query().get()
        # TODO: Would it be better without the question mark?
        self.travelperk.get.assert_called_once_with("invoices?")
        self.assert_equals_invoices_stub(invoices)

    def test_getting_an_invoice_detail(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoice.json")
        invoice = self.invoices.get("serialNumber")
        self.travelperk.get.assert_called_once_with("invoices/serialNumber")
        assert invoice.serial_number == "INV-01-987654"
        assert invoice.profile_id == "edb6322b-8e11-48e9-8d6f-6402e445e50d"
        assert invoice.profile_name == "My Company Ltd"
        assert invoice.billing_information.legal_name == "My Company Ltd"
        assert invoice.billing_information.vat_number == "GB123456789"
        assert invoice.billing_information.address_line_1 == "199 Bishopsgate"
        assert invoice.billing_information.address_line_2 == "Spitalfields"
        assert invoice.billing_information.city == "London"
        assert invoice.billing_information.postal_code == "EC2M 3TY"
        assert invoice.billing_information.country_name == "United Kingdom"
        assert invoice.mode == "reseller"
        assert invoice.status == "paid"
        assert invoice.issuing_date == "2020-03-31"
        assert invoice.billing_period == "monthly"
        assert invoice.from_date == "2020-03-01"
        assert invoice.to_date == "2020-03-31"
        assert invoice.due_date == "2020-04-15"
        assert invoice.currency == "EUR"
        assert invoice.total == "13579.24"
        assert invoice.lines.total == "1"
        assert len(invoice.lines.data) == 1
        assert invoice.lines.data[0].expense_date == "2020-02-13"
        assert invoice.lines.data[0].description == "FLIGHT for Trip ID 1687664"
        assert invoice.lines.data[0].quantity == 1
        assert invoice.lines.data[0].unit_price == "20.00000000"
        assert invoice.lines.data[0].non_taxable_unit_price == "0E-8"
        assert invoice.lines.data[0].tax_percentage == "0E-8"
        assert invoice.lines.data[0].tax_amount == "0E-8"
        assert invoice.lines.data[0].tax_regime == "STAR"
        assert invoice.lines.data[0].total_amount == "20.00000000"
        assert invoice.lines.data[0].invoice_serial_number == "INV-01-190111"
        assert (
            invoice.lines.data[0].profile_id == "09d649d1-35fa-4d9f-b688-046d5790afd2"
        )
        assert invoice.lines.data[0].profile_name == "My Company Ltd"
        assert invoice.lines.data[0].invoice_mode == "reseller"
        assert invoice.lines.data[0].invoice_status == "paid"
        assert invoice.lines.data[0].issuing_date == "2020-02-13"
        assert invoice.lines.data[0].due_date == "2020-02-13"
        assert invoice.lines.data[0].currency == "EUR"
        assert invoice.lines.data[0].metadata.trip_id == 1687664
        assert (
            invoice.lines.data[0].metadata.trip_name
            == "Meeting with German company GmbH"
        )
        assert invoice.lines.data[0].metadata.service == "flight"
        assert len(invoice.lines.data[0].metadata.travelers) == 1
        assert invoice.lines.data[0].metadata.travelers[0].name == "John Doe"
        assert (
            invoice.lines.data[0].metadata.travelers[0].email
            == "john.doe@mycompany.com"
        )
        assert invoice.lines.data[0].metadata.travelers[0].external_id == "ASD123"
        assert invoice.lines.data[0].metadata.start_date == "2020-03-27"
        assert invoice.lines.data[0].metadata.end_date == "2020-04-05"
        assert invoice.lines.data[0].metadata.cost_center == "DACH Accounts"
        assert invoice.lines.data[0].metadata.labels == ["Sales trips", "Special"]
        assert invoice.lines.data[0].metadata.vendor.code == "LH"
        assert invoice.lines.data[0].metadata.vendor.name == "Lufthansa"
        assert invoice.lines.data[0].metadata.out_of_policy is False
        assert len(invoice.lines.data[0].metadata.approvers) == 1
        assert invoice.lines.data[0].metadata.approvers[0].name == "Jake Bolt"
        assert (
            invoice.lines.data[0].metadata.approvers[0].email
            == "jake.bolt@mycompany.com"
        )
        assert invoice.lines.data[0].metadata.approvers[0].external_id == "ASD124"
        assert invoice.lines.data[0].metadata.booker.name == "Marien Lint"
        assert (
            invoice.lines.data[0].metadata.booker.email == "marien.lint@mycompany.com"
        )
        assert invoice.lines.data[0].metadata.booker.external_id == "ASD124"
        assert (
            invoice.lines.next
            == "/invoices/lines?serial_number=INV-01-987654&offset=10"
        )
        assert len(invoice.taxes_summary) == 2
        assert invoice.taxes_summary[0].tax_regime == "STAR"
        assert invoice.taxes_summary[0].subtotal == "6543.21"
        assert invoice.taxes_summary[0].tax_percentage == "0.00"
        assert invoice.taxes_summary[0].tax_amount == "0.00"
        assert invoice.taxes_summary[0].total == "6543.21"
        assert invoice.taxes_summary[1].tax_regime == "G-VAT-R"
        assert invoice.taxes_summary[1].subtotal == "5912.63"
        assert invoice.taxes_summary[1].tax_percentage == "19.00"
        assert invoice.taxes_summary[1].tax_amount == "1123.40"
        assert invoice.taxes_summary[1].total == "7036.03"
        assert invoice.reference == "My Company Ltd - SEPA - Monthly 2020-03"
        assert invoice.travelperk_bank_account.bank_name == "La Caixa"
        assert (
            invoice.travelperk_bank_account.account_number
            == "ES01 2345 6789 1098 7654 3210"
        )
        assert invoice.travelperk_bank_account.bic == "CAIX ES BB XXX"
        assert invoice.travelperk_bank_account.reference == "INV-01-987654"
        assert invoice.pdf == "https://api.travelperk.com/invoices/INV-01-987654/pdf"

    def test_getting_an_invoice_pdf(self):
        self.travelperk.get.return_value = "invoicePDF"
        assert self.invoices.pdf("serialNumber") == "invoicePDF"
        self.travelperk.get.assert_called_once_with("invoices/serialNumber/pdf")

    def test_getting_all_invoice_lines_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoice_lines.json")
        params = InvoiceLinesInputParams().set_offset(5).set_limit(10)
        invoice_lines = self.invoices.lines(params)
        self.travelperk.get.assert_called_once_with("invoices/lines?offset=5&limit=10")
        self.assert_equals_stub(invoice_lines)

    def test_getting_all_invoice_lines_with_params_using_query(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoice_lines.json")
        invoice_lines = self.invoices.lines_query().set_offset(5).set_limit(10).get()
        self.travelperk.get.assert_called_once_with("invoices/lines?offset=5&limit=10")
        self.assert_equals_stub(invoice_lines)

    def test_getting_all_invoice_lines_no_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("invoice_lines.json")
        invoice_lines = self.invoices.lines()
        self.assert_equals_stub(invoice_lines)

    """
    def test_getting_all_billing_periods(self):
        self.assertEquals(
            [
                'instant',
                'weekly',
                'biweekly',
                'monthly',
            ],
            self.invoices.billing_periods()
        )

    def test_getting_all_statuses(self):
        self.assertEquals(
            [
                'draft',
                'open',
                'paid',
                'unpaid',
            ],
            self.invoices.statuses()
        )

    def test_getting_all_sorting_values(self):
        self.assertEquals(
            [
                'issuing_date',
                '-issuing_date',
            ],
            self.invoices.sorting()
        )
    """
