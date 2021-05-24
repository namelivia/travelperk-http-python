import datetime
from typing import List, TYPE_CHECKING
from .invoices_input_params import InvoicesInputParams
from travelperk_python_api_types.expenses.invoices.invoices import (
    Invoices as InvoicesType,
)

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class InvoicesQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = InvoicesInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str):
        return getattr(self.travelperk, method)(url)

    def get(self) -> InvoicesType:
        return InvoicesType(
            **self.execute(
                "get", "/".join(["invoices"]) + "?" + self.params.as_url_param()
            )
        )

    def set_profile_id(self, profile_id: List[str]) -> "InvoicesQuery":
        self.params.set_profile_id(profile_id)
        return self

    def set_serial_number(self, serial_number: List[str]) -> "InvoicesQuery":
        self.params.set_serial_number(serial_number)
        return self

    def set_serial_contains(self, serial_number_contains: str) -> "InvoicesQuery":
        self.params.set_serial_contains(serial_number_contains)
        return self

    def set_billing_period(self, billing_period: str) -> "InvoicesQuery":
        self.params.set_billing_period(billing_period)

    def set_travelperk_bank_account_number(
        self, account_number: str
    ) -> "InvoicesQuery":
        self.params.set_travelperk_bank_account_number(account_number)
        return self

    def set_customer_country_name(self, customer_country_name: str) -> "InvoicesQuery":
        self.params.set_customer_country_name(customer_country_name)
        return self

    def set_status(self, status: str) -> "InvoicesQuery":
        self.params.set_status(status)
        return self

    def set_issuing_date_gte(self, issuing_date_gte: datetime) -> "InvoicesQuery":
        self.params.set_issuing_date_gte(issuing_date_gte)
        return self

    def set_issuing_date_lte(self, issuing_date_lte: datetime) -> "InvoicesQuery":
        self.params.set_issuing_date_lte(issuing_date_lte)
        return self

    def set_due_date_gte(self, due_date_gte: datetime) -> "InvoicesQuery":
        self.params.set_due_date_gte(due_date_gte)
        return self

    def set_due_date_lte(self, due_date_lte: datetime) -> "InvoicesQuery":
        self.params.set_due_date_lte(due_date_lte)
        return self

    def set_sort(self, sort: str) -> "InvoicesQuery":
        self.params.set_sort(sort)
        return self

    def set_offset(self, offset: int) -> "InvoicesQuery":
        self.params.set_offset(offset)
        return self

    def set_limit(self, limit: str) -> "InvoicesQuery":
        self.params.set_limit(limit)
        return self
