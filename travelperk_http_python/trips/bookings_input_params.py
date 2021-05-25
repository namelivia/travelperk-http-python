import urllib
import datetime
from .type import Type
from .booking_status import BookingStatus


class BookingsInputParams:
    def __init__(self):
        self.modified_gte = None
        self.modified_lt = None
        self.status = None
        self.type = None
        self.offset = None
        self.limit = None

    def set_modified_lt(self, modified_lt: datetime) -> "BookingsInputParams":
        self.modified_lt = modified_lt
        return self

    def set_modified_gte(self, modified_gte: datetime) -> "BookingsInputParams":
        self.modified_gte = modified_gte
        return self

    def set_status(self, status: str) -> "BookingsInputParams":
        self.status = BookingStatus(status)
        return self

    def set_type(self, _type: str) -> "BookingsInputParams":
        self.type = Type(_type)
        return self

    def set_offset(self, offset: int) -> "BookingsInputParams":
        self.offset = offset
        return self

    def set_limit(self, limit: int) -> "BookingsInputParams":
        self.limit = limit
        return self

    def as_url_param(self) -> str:
        data = {
            "modified_lt": self.modified_lt.strftime("%Y-%m-%d")
            if self.modified_lt is not None
            else None,
            "modified_gte": self.modified_gte.strftime("%Y-%m-%d")
            if self.modified_gte is not None
            else None,
            "status": self.status.value if self.status is not None else None,
            "type": self.type.value if self.type is not None else None,
            "offset": self.offset,
            "limit": self.limit,
        }
        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
