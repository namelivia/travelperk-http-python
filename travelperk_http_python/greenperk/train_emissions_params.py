import urllib


class TrainEmissionsParams:
    def __init__(self, origin_id: str, destination_id: str, vendor: str = None):
        self.set_origin_id(origin_id)
        self.set_destination_id(destination_id)
        self.set_vendor(vendor)

    def set_origin_id(self, origin_id: str) -> "TrainEmissionsParams":
        self.origin_id = origin_id
        return self

    def set_destination_id(self, destination_id: str) -> "TrainEmissionsParams":
        self.destination_id = destination_id
        return self

    def set_vendor(self, vendor: str) -> "TrainEmissionsParams":
        self.vendor = vendor
        return self

    def as_url_param(self) -> str:
        data = {
            "origin_id": self.origin_id,
            "destination_id": self.destination_id,
            "vendor": self.vendor if self.vendor is not None else None,
        }
        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
