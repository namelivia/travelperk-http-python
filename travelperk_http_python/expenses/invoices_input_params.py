import datetime
import urllib
from typing import List
from .status import Status
from .billing_period import BillingPeriod
from .sorting import Sorting


class InvoicesInputParams:
    def __init__(self):
        self.profile_id = None
        self.serial_number = None
        self.serial_number_contains = None
        self.billing_period = None
        self.account_number = None
        self.customer_country_name = None
        self.status = None
        self.issuing_date_gte = None
        self.issuing_date_lte = None
        self.due_date_gte = None
        self.due_date_lte = None
        self.offset = None
        self.limit = None
        self.sort = None

    def set_profile_id(self, profile_id: List[str]) -> "InvoicesInputParams":
        self.profile_id = profile_id
        return self

    def set_serial_number(self, serial_number: List[str]) -> "InvoicesInputParams":
        self.serial_number = serial_number
        return self

    def set_serial_contains(self, serial_number_contains: str) -> "InvoicesInputParams":
        self.serial_number_contains = serial_number_contains
        return self

    def set_billing_period(self, billing_period: str) -> "InvoicesInputParams":
        self.billing_period = BillingPeriod(billing_period)
        return self

    def set_travelperk_bank_account_number(
        self, account_number: str
    ) -> "InvoicesInputParams":
        self.account_number = account_number
        return self

    def set_customer_country_name(
        self, customer_country_name: str
    ) -> "InvoicesInputParams":
        self.customer_country_name = customer_country_name
        return self

    def set_status(self, status: str) -> "InvoicesInputParams":
        self.status = Status(status)
        return self

    def set_issuing_date_gte(self, issuing_date_gte: datetime) -> "InvoicesInputParams":
        self.issuing_date_gte = issuing_date_gte
        return self

    def set_issuing_date_lte(self, issuing_date_lte: datetime) -> "InvoicesInputParams":
        self.issuing_date_lte = issuing_date_lte
        return self

    def set_due_date_gte(self, due_date_gte: datetime) -> "InvoicesInputParams":
        self.due_date_gte = due_date_gte
        return self

    def set_due_date_lte(self, due_date_lte: datetime) -> "InvoicesInputParams":
        self.due_date_lte = due_date_lte
        return self

    def set_sort(self, sort: str) -> "InvoicesInputParams":
        self.sort = Sorting(sort)
        return self

    def set_offset(self, offset: int) -> "InvoicesInputParams":
        self.offset = offset
        return self

    def set_limit(self, limit: int) -> "InvoicesInputParams":
        self.limit = limit
        return self

    def as_url_param(self) -> str:
        data = {
            "profile_id": ",".join(self.profile_id)
            if self.profile_id is not None
            else None,
            "serial_number": ",".join(self.serial_number)
            if self.serial_number
            else None,
            "serial_number_contains": self.serial_number_contains,
            "billing_period": self.billing_period.value
            if self.billing_period is not None
            else None,
            "travelperk_bank_account_number": self.account_number,
            "customer_country_name": self.customer_country_name,
            "status": self.status.value if self.status is not None else None,
            "issuing_date_gte": self.issuing_date_gte.strftime("%Y-%m-%d")
            if self.issuing_date_gte is not None
            else None,
            "issuing_date_lte": self.issuing_date_lte.strftime("%Y-%m-%d")
            if self.issuing_date_lte is not None
            else None,
            "due_date_gte": self.due_date_gte.strftime("%Y-%m-%d")
            if self.due_date_gte is not None
            else None,
            "due_date_lte": self.due_date_lte.strftime("%Y-%m-%d")
            if self.due_date_lte is not None
            else None,
            "offset": self.offset,
            "limit": self.limit,
            "sort": self.sort.value if self.sort is not None else None,
        }

        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
