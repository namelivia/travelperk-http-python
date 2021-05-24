import urllib


class UsersInputParams:
    def __init__(self):
        self.count = None
        self.start_index = None
        self._filter = None

    def set_count(self, count: int) -> "UsersInputParams":
        self.count = count
        return self

    def set_start_index(self, start_index: int) -> "UsersInputParams":
        self.start_index = start_index
        return self

    def set_filter(self, _filter: str) -> "UsersInputParams":
        self._filter = _filter
        return self

    def as_url_param(self) -> str:
        data = {
            "count": self.count,
            "startIndex": self.start_index,
            "filter": self._filter,
        }
        return urllib.parse.urlencode({k: v for k, v in data.items() if v is not None})
