# import json
import humps
import datetime
from typing import List, TYPE_CHECKING
from travelperk_http_python.scim.name_input_params import NameInputParams
from travelperk_http_python.scim.replace_user_input_params import ReplaceUserInputParams
from travelperk_http_python.scim.emergency_contact import EmergencyContact
from travelperk_python_api_types.scim.users.user import User

if TYPE_CHECKING:
    from travelperk_http_python.api.travelperk import TravelPerk


class ModifyUserRequest:
    def __init__(
        self,
        id: int,
        travelperk: "TravelPerk",
        username: str,
        active: bool,
        name: NameInputParams,
    ):
        self.id = id
        self.params = ReplaceUserInputParams(username, active, name)
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: List[str] = None):
        if params is None:
            response = getattr(self.travelperk, method)(url)
        else:
            response = getattr(self.travelperk, method)(url, params)

        # TODO: This won't go here. Ugly fix!
        try:
            response["travelperk_extension"] = response[
                "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"
            ]
            del response["urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"]
        except KeyError:
            pass
        try:
            response["enterprise_extension"] = response[
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ]
            del response["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]
        except KeyError:
            pass
        try:
            response["enterprise_extension"]["manager"]["ref"] = response[
                "enterprise_extension"
            ]["manager"]["$ref"]
            del response["enterprise_extension"]["manager"]["$ref"]
        except KeyError:
            pass
        # TODO
        return response

    def save(self) -> User:
        return User(
            **humps.decamelize(
                self.execute(
                    "put",
                    "/".join(["scim", "Users", str(self.id)]),
                    self.params.to_dict(),
                )
            )
        )

    def set_language(self, language: str) -> "ModifyUserRequest":
        self.params.set_language(language)
        return self

    def set_locale(self, locale: str) -> "ModifyUserRequest":
        self.params.set_locale(locale)
        return self

    def set_title(self, title: str) -> "ModifyUserRequest":
        self.params.set_title(title)
        return self

    def set_external_id(self, external_id: str) -> "ModifyUserRequest":
        self.params.set_external_id(external_id)
        return self

    def set_phone_number(self, number: str) -> "ModifyUserRequest":
        self.params.set_phone_number(number)
        return self

    def set_gender(self, gender: str) -> "ModifyUserRequest":
        self.params.set_gender(gender)
        return self

    def set_date_of_birth(self, date_of_birth: datetime) -> "ModifyUserRequest":
        self.params.set_date_of_birth(date_of_birth)
        return self

    def set_travel_policy(self, travel_policy: str) -> "ModifyUserRequest":
        self.params.set_travel_policy(travel_policy)
        return self

    def set_emergency_contact(
        self, emergency_contact_name: str, emergency_contact_phone: str
    ) -> "ModifyUserRequest":
        emergency_contact = EmergencyContact(
            emergency_contact_name, emergency_contact_phone
        )
        self.params.set_emergency_contact(emergency_contact)
        return self

    def set_invoice_profiles(self, invoice_profiles: List[str]) -> "ModifyUserRequest":
        self.params.set_invoice_profiles(invoice_profiles)
        return self

    def set_cost_center(self, cost_center: str) -> "ModifyUserRequest":
        self.params.set_cost_center(cost_center)
        return self

    def set_manager(self, manager: str) -> "ModifyUserRequest":
        self.params.set_manager(manager)
        return self

    def set_honorific_prefix(self, honorific_prefix: str) -> "ModifyUserRequest":
        self.params.set_honorific_prefix(honorific_prefix)
        return self

    def set_middle_name(self, middle_name: str) -> "ModifyUserRequest":
        self.params.set_middle_name(middle_name)
        return self

    def _has_custom_user_data(self) -> bool:
        return self.params.has_custom_user_data()

    def _has_enterprise_data(self) -> bool:
        return self.params.has_enterprise_data()
