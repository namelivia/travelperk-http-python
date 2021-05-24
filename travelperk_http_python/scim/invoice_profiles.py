from typing import List


class InvoiceProfiles:
    def __init__(self, invoice_profiles: List[str]):
        self.invoice_profiles = invoice_profiles

    def as_list(self) -> List:
        return [{"value": invoice_profile} for invoice_profile in self.invoice_profiles]
