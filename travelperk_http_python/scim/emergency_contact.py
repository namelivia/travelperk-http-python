class EmergencyContact:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
        }
