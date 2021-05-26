class NameInputParams:
    def __init__(self, given_name: str, family_name: str):
        self.given_name = given_name
        self.family_name = family_name
        self.honorific_prefix = None
        self.middle_name = None

    def set_honorific_prefix(self, honorific_prefix: str) -> "NameInputParams":
        self.honorific_prefix = honorific_prefix
        return self

    def set_middle_name(self, middle_name: str) -> "NameInputParams":
        self.middle_name = middle_name
        return self

    def to_dict(self) -> dict:
        data = {
            "givenName": self.given_name,
            "familyName": self.family_name,
            "honorificPrefix": self.honorific_prefix,
            "middleName": self.middle_name,
        }
        return {k: v for k, v in data.items() if v is not None}
