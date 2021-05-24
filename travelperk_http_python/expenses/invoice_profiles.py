from typing import TYPE_CHECKING
from .invoice_profiles_query import InvoiceProfilesQuery

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class InvoiceProfiles:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # Query invoice profiles.
    def query(self) -> InvoiceProfilesQuery:
        return InvoiceProfilesQuery(self.travelperk)
