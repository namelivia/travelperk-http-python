import urllib


class UsersInputParams:
    def __init__(self):
        self.trip_id = None
        self.offset = None
        self.limit = None

    def set_trip_id(self, trip_id: str) -> "UsersInputParams":
        self.trip_id = trip_id
        return self

    def set_offset(self, offset: int) -> "UsersInputParams":
        self.offset = offset
        return self

    def set_limit(self, limit: int) -> "UsersInputParams":
        self.limit = limit
        return self

    def as_url_param(self) -> str:
        data = {
            "trip_id": self.trip_id,
            "offset": self.offset,
            "limit": self.limit,
        }
        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
