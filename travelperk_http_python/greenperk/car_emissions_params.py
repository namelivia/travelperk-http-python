import urllib


class CarEmissionsParams:
    def __init__(self, acriss_code: str, num_days: int, distance_per_day: int):
        self.set_acriss_code(acriss_code)
        self.set_num_days(num_days)
        self.set_distance_per_day(distance_per_day)

    def set_acriss_code(self, acriss_code: str) -> "CarEmissionsParams":
        self.acriss_code = acriss_code
        return self

    def set_num_days(self, num_days: int) -> "CarEmissionsParams":
        self.num_days = num_days
        return self

    def set_distance_per_day(self, distance_per_day: int) -> "CarEmissionsParams":
        self.distance_per_day = distance_per_day
        return self

    def as_url_param(self) -> str:
        return urllib.parse.urlencode(
            {
                "acriss_code": self.acriss_code,
                "num_days": self.num_days,
                "distance_per_day": self.distance_per_day,
            }
        )
