from typing import TYPE_CHECKING
from travelperk_http_python.expenses.invoices import Invoices
from travelperk_http_python.expenses.invoice_profiles import InvoiceProfiles

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class ExpensesAPI:
    def __init__(self, travelperk: "TravelPerk"):
        self._invoce_profiles = InvoiceProfiles(travelperk)
        self._invoces = Invoices(travelperk)

    def invoice_profiles(self) -> InvoiceProfiles:
        return self._invoce_profiles

    def invoices(self) -> Invoices:
        return self._invoces
