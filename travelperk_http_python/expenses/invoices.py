from typing import List, TYPE_CHECKING
from .invoices_query import InvoicesQuery
from .invoice_lines_input_params import InvoiceLinesInputParams
from .invoice_lines_query import InvoiceLinesQuery
from .status import Status
from .billing_period import BillingPeriod
from .sorting import Sorting
from travelperk_python_api_types.expenses.invoices.invoice import (
    Invoice as InvoiceType,
)
from travelperk_python_api_types.expenses.invoice_lines.invoice_lines import (
    InvoiceLines as InvoiceLinesType,
)

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class Invoices:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str):
        return getattr(self.travelperk, method)(url)

    # Query invoices.
    def query(self) -> InvoicesQuery:
        return InvoicesQuery(self.travelperk)

    # Get invoice detail.
    def get(self, serial_number: str) -> InvoiceType:
        return InvoiceType(**self.execute("get", "/".join(["invoices", serial_number])))

    # Get invoice in PDF format.
    def pdf(self, serial_number: str) -> str:
        return self.travelperk.get("/".join(["invoices", serial_number, "pdf"]))

    # Get list of invoices lines.
    def lines(self, params: InvoiceLinesInputParams = None) -> InvoiceLinesType:
        params = "?" + params.as_url_param() if params is not None else ""
        return InvoiceLinesType(
            **self.execute("get", "/".join(["invoices", "lines"]) + params)
        )

    # Query the invoices lines.
    def lines_query(self) -> InvoiceLinesQuery:
        return InvoiceLinesQuery(self.travelperk)

    # Get all billing periods.
    def billing_periods(self) -> List[str]:
        return [billing_period.value for billing_period in BillingPeriod]

    # Get all statuses.
    def statuses(self) -> List[str]:
        return [status.value for status in Status]

    # Get all sorting values.
    def sorting(self) -> List[str]:
        return [sorting.value for sorting in Sorting]
