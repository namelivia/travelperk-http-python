import datetime
import urllib
from .status import Status


class TripsInputParams:
    def __init__(self):
        self.modified_gte = None
        self.modified_lt = None
        self.status = None
        self.offset = None
        self.limit = None

    def set_modified_lt(self, modified_lt: datetime) -> "TripsInputParams":
        self.modified_lt = modified_lt
        return self

    def set_modified_gte(self, modified_gte: datetime) -> "TripsInputParams":
        self.modified_gte = modified_gte
        return self

    def set_status(self, status: str) -> "TripsInputParams":
        self.status = Status(status)
        return self

    def set_offset(self, offset: int) -> "TripsInputParams":
        self.offset = offset
        return self

    def set_limit(self, limit: int) -> "TripsInputParams":
        self.limit = limit
        return self

    def as_url_param(self) -> str:
        data = {
            "modified_lt": self.modified_lt.format("%Y-%m-%d")
            if self.modified_lt is not None
            else None,
            "modified_gte": self.modified_gte.format("%Y-%m-%d")
            if self.modified_gte is not None
            else None,
            "status": self.status.value if self.status is not None else None,
            "offset": self.offset,
            "limit": self.limit,
        }
        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
