import urllib


class HotelEmissionsParams:
    def __init__(self, country_code: str, num_nights: int):
        self.set_country_code(country_code)
        self.set_num_nights(num_nights)

    def set_country_code(self, country_code: str) -> "HotelEmissionsParams":
        self.country_code = country_code
        return self

    def set_num_nights(self, num_nights: str) -> "HotelEmissionsParams":
        self.num_nights = num_nights
        return self

    def as_url_param(self) -> str:
        return urllib.parse.urlencode(
            {
                "country_code": self.country_code,
                "num_nights": self.num_nights,
            }
        )
