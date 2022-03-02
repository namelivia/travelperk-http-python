import urllib


class FlightEmissionsParams:
    def __init__(
        self, origin: str, destination: str, cabin_class: str, airline_code: str
    ):
        self.set_origin(origin)
        self.set_destination(destination)
        self.set_cabin_class(cabin_class)
        self.set_airline_code(airline_code)

    def set_origin(self, origin: str) -> "FlightEmissionsParams":
        self.origin = origin
        return self

    def set_destination(self, destination: str) -> "FlightEmissionsParams":
        self.destination = destination
        return self

    def set_cabin_class(self, cabin_class: str) -> "FlightEmissionsParams":
        self.cabin_class = cabin_class
        return self

    def set_airline_code(self, airline_code: str) -> "FlightEmissionsParams":
        self.airline_code = airline_code
        return self

    def as_url_param(self) -> str:
        return urllib.parse.urlencode(
            {
                "origin": self.origin,
                "destination": self.destination,
                "cabin_class": self.cabin_class,
                "airline_code": self.airline_code,
            }
        )
