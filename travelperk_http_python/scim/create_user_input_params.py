import datetime
from typing import List
from travelperk_http_python.scim.name_input_params import NameInputParams
from travelperk_http_python.scim.language import Language
from travelperk_http_python.scim.gender import Gender
from travelperk_http_python.scim.emergency_contact import EmergencyContact
from travelperk_http_python.scim.invoice_profiles import InvoiceProfiles


class CreateUserInputParams:
    def __init__(self, user_name: str, active: bool, name: NameInputParams):
        self.user_name = user_name
        self.active = active
        self.name = name
        self.language = None
        self.locale = None
        self.title = None
        self.external_id = None
        self.phone_number = None
        self.gender = None
        self.date_of_birth = None
        self.travel_policy = None
        self.invoice_profiles = None
        self.emergency_contact = None
        self.cost_center = None
        self.manager = None

    def set_language(self, language: str) -> "CreateUserInputParams":
        self.language = Language(language)
        return self

    def set_locale(self, locale: str) -> "CreateUserInputParams":
        self.locale = locale
        return self

    def set_title(self, title: str) -> "CreateUserInputParams":
        self.title = title
        return self

    def set_external_id(self, external_id: str) -> "CreateUserInputParams":
        self.external_id = external_id
        return self

    def set_phone_number(self, number: str) -> "CreateUserInputParams":
        self.phone_number = number
        return self

    def set_gender(self, gender: str) -> "CreateUserInputParams":
        self.gender = Gender(gender)
        return self

    def set_date_of_birth(self, date_of_birth: datetime) -> "CreateUserInputParams":
        self.date_of_birth = date_of_birth
        return self

    def set_travel_policy(self, travel_policy: str) -> "CreateUserInputParams":
        self.travel_policy = travel_policy
        return self

    def set_emergency_contact(
        self, emergency_contact: EmergencyContact
    ) -> "CreateUserInputParams":
        self.emergency_contact = emergency_contact
        return self

    def set_invoice_profiles(
        self, invoice_profiles: List[str]
    ) -> "CreateUserInputParams":
        self.invoice_profiles = InvoiceProfiles(invoice_profiles)
        return self

    def set_cost_center(self, cost_center: str) -> "CreateUserInputParams":
        self.cost_center = cost_center
        return self

    def set_manager(self, manager: str) -> "CreateUserInputParams":
        self.manager = manager
        return self

    def set_honorific_prefix(self, honorific_prefix: str) -> "CreateUserInputParams":
        self.name.set_honorific_prefix(honorific_prefix)
        return self

    def set_middle_name(self, middle_name) -> "CreateUserInputParams":
        self.name.set_middle_name(middle_name)
        return self

    def _has_custom_user_data(self) -> bool:
        # TODO: Filter None values
        customer_data = [
            self.gender,
            self.date_of_birth,
            self.travel_policy,
            None if self.invoice_profiles is None else self.invoice_profiles,
            self.emergency_contact,
        ]
        return len(customer_data) > 0

    def _has_enterprise_data(self) -> bool:
        # TODO: Filter None values
        enterprise_data = [
            self.cost_center,
            self.manager,
        ]
        return len(enterprise_data) > 0

    def to_dict(self) -> dict:
        data = {
            "userName": self.user_name,
            "name": self.name.to_dict(),
            "active": self.active,
            "preferredLanguage": self.language.value
            if self.language is not None
            else None,
            "locale": self.locale,
            "title": self.title,
            "externalId": self.external_id,
            "phoneNumbers": None
            if self.phone_number is None
            else [
                {
                    "value": self.phone_number,
                    "type": "work",
                },
            ],
        }

        if self._has_custom_user_data():
            travelperk_extension = {
                "gender": self.gender.value if self.gender is not None else None,
                "dateOfBirth": self.date_of_birth.strftime("%Y/%m/%d")
                if self.date_of_birth is not None
                else None,
                "travelPolicy": self.travel_policy,
                "emergencyContact": self.emergency_contact.to_dict()
                if self.emergency_contact is not None
                else None,
                "invoiceProfiles": self.invoice_profiles.as_list()
                if self.invoice_profiles is not None
                else None,
            }
            travelperk_extension = {
                k: v for k, v in travelperk_extension.items() if v is not None
            }
            if travelperk_extension:
                data[
                    "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"
                ] = travelperk_extension

        if self._has_enterprise_data():
            enterprise_extension = {
                "costCenter": self.cost_center
                if self.cost_center is not None
                else None,
                "manager": {"value": self.manager}
                if self.manager is not None
                else None,
            }
            enterprise_extension = {
                k: v for k, v in enterprise_extension.items() if v is not None
            }
            if enterprise_extension:
                data[
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ] = enterprise_extension
        return {k: v for k, v in data.items() if v is not None}
