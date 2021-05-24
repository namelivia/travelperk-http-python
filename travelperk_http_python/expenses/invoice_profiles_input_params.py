import urllib


class InvoiceProfilesInputParams:
    def __init__(self):
        self.limit = None
        self.offset = None

    def set_offset(self, offset: int) -> "InvoiceProfilesInputParams":
        self.offset = offset
        return self

    def set_limit(self, limit: int) -> "InvoiceProfilesInputParams":
        self.limit = limit
        return self

    def as_url_param(self) -> dict:
        data = {
            "offset": self.offset,
            "limit": self.limit,
        }

        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
