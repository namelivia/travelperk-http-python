import urllib
import datetime
from freezegun import freeze_time
from travelperk_http_python.expenses.invoice_lines_input_params import (
    InvoiceLinesInputParams,
)
from travelperk_http_python.expenses.status import Status
from travelperk_http_python.expenses.billing_period import BillingPeriod


class TestInvoiceLinesInputParam:
    @freeze_time("2013-04-12")
    def test_setting_invoice_lines_all_input_params(self):
        input_params = InvoiceLinesInputParams()
        input_params.set_profile_id(["profile_id1", "profile_id2"]).set_serial_number(
            ["serial_number1", "serial_number2"]
        ).set_serial_contains("serial_number_contains").set_billing_period(
            BillingPeriod.MONTHLY
        ).set_travelperk_bank_account_number(
            "bank_account_number"
        ).set_customer_country_name(
            "customer_country_name"
        ).set_status(
            Status.PAID
        ).set_issuing_date_gte(
            datetime.date.today()
        ).set_issuing_date_lte(
            datetime.date.today() + datetime.timedelta(days=1)
        ).set_due_date_gte(
            datetime.date.today() - datetime.timedelta(days=1)
        ).set_due_date_lte(
            datetime.date.today() + datetime.timedelta(days=10)
        ).set_expense_date_gte(
            datetime.date.today() - datetime.timedelta(days=10)
        ).set_expense_date_lte(
            datetime.date.today() - datetime.timedelta(days=10)
        ).set_offset(
            32
        ).set_limit(
            64
        )
        assert (
            "profile_id=profile_id1,profile_id2&"
            + "serial_number=serial_number1,serial_number2&"
            + "serial_number_contains=serial_number_contains&"
            + "billing_period=monthly&"
            + "travelperk_bank_account_number=bank_account_number&"
            + "customer_country_name=customer_country_name&"
            + "status=paid&"
            + "issuing_date_gte=2013-04-12&"
            + "issuing_date_lte=2013-04-13&"
            + "due_date_gte=2013-04-11&"
            + "due_date_lte=2013-04-22&"
            + "expense_date_gte=2013-04-02&"
            + "expense_date_lte=2013-04-02&"
            + "offset=32&"
            + "limit=64"
        ) == urllib.parse.unquote(input_params.as_url_param())

    def test_setting_invoice_lines_some_input_params(self):
        input_params = InvoiceLinesInputParams()
        input_params.set_serial_number(["serial_number1", "serial_number2"]).set_status(
            Status.PAID
        )
        assert (
            "serial_number=serial_number1,serial_number2&status=paid"
            == urllib.parse.unquote(input_params.as_url_param())
        )

    def test_setting_invoice_lines_no_input_params(self):
        input_params = InvoiceLinesInputParams()
        assert "" == urllib.parse.unquote(input_params.as_url_param())
