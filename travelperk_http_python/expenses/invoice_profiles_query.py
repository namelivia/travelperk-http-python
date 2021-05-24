from typing import TYPE_CHECKING
from travelperk_python_api_types.expenses.invoice_profiles.invoice_profiles import (
    InvoiceProfiles as InvoiceProfilesType,
)
from .invoice_profiles_input_params import InvoiceProfilesInputParams

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class InvoiceProfilesQuery:
    def __init__(self, travelperk: "TravelPerk"):
        self.params = InvoiceProfilesInputParams()
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str):
        return getattr(self.travelperk, method)(url)

    def set_offset(self, offset: int) -> "InvoiceProfilesQuery":
        self.params.set_offset(offset)
        return self

    def set_limit(self, limit: int) -> "InvoiceProfilesQuery":
        self.params.set_limit(limit)
        return self

    def get(self) -> InvoiceProfilesType:
        return InvoiceProfilesType(
            **self.execute(
                "get", "/".join(["profiles"]) + "?" + self.params.as_url_param()
            )
        )
