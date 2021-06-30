from typing import List, TYPE_CHECKING
import humps
from travelperk_http_python.scim.users_query import UsersQuery
from travelperk_python_api_types.scim.users.user import User
from travelperk_http_python.scim.create_user_query import CreateUserQuery
from travelperk_http_python.scim.name_input_params import NameInputParams
from travelperk_http_python.scim.create_user_input_params import CreateUserInputParams
from travelperk_http_python.scim.replace_user_input_params import ReplaceUserInputParams
from travelperk_http_python.scim.update_user_input_params import UpdateUserInputParams
from travelperk_http_python.scim.modify_user_request import ModifyUserRequest
from travelperk_http_python.scim.language import Language
from travelperk_http_python.scim.gender import Gender

if TYPE_CHECKING:
    from api.travelperk import TravelPerk


class Users:
    def __init__(self, travelperk: "TravelPerk"):
        self.travelperk = travelperk

    # TODO: This is temporary
    def execute(self, method: str, url: str, params: dict = None):
        if params is None:
            response = getattr(self.travelperk, method)(url)
        else:
            response = getattr(self.travelperk, method)(url, params)

        # TODO: This won't go here. Ugly fix!
        response["travelperk_extension"] = response[
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"
        ]
        del response["urn:ietf:params:scim:schemas:extension:travelperk:2.0:User"]
        response["enterprise_extension"] = response[
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
        ]
        del response["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]
        try:
            response["enterprise_extension"]["manager"]["ref"] = response[
                "enterprise_extension"
            ]["manager"]["$ref"]
            del response["enterprise_extension"]["manager"]["$ref"]
        except KeyError:
            pass
        # TODO

        return response

    # Query users.
    def query(self) -> UsersQuery:
        return UsersQuery(self.travelperk)

    # Retrieve a user from TravelPerk.
    def get(self, id: int) -> User:
        return User(
            **humps.decamelize(
                self.execute("get", "/".join(["scim", "Users", str(id)]))
            )
        )

    # Deletes a user from TravelPerk.
    def delete(self, id: int) -> str:
        return self.travelperk.delete("/".join(["scim", "Users", str(id)]))

    # Make a new user in TravelPerk.
    def make(
        self, username: str, active: bool, given_name: str, family_name: str
    ) -> CreateUserQuery:
        name = NameInputParams(given_name, family_name)
        return CreateUserQuery(self.travelperk, username, active, name)

    # Create a new user in TravelPerk.
    def create(
        self, username: str, active: bool, given_name: str, family_name: str
    ) -> User:
        name = NameInputParams(given_name, family_name)
        params = CreateUserInputParams(username, active, name)
        return User(
            **humps.decamelize(
                self.execute("post", "/".join(["scim", "Users"]), params.to_dict())
            )
        )

    # Update an existing user in TravelPerk.
    def update(self, id: int, params: UpdateUserInputParams) -> User:
        # TODO: Open and link an issue here
        raise NotImplementedError()

    # Replace an existing user in TravelPerk.
    def replace(self, id: int, params: ReplaceUserInputParams) -> User:
        return User(
            **humps.decamelize(
                self.execute("put", "/".join(["scim", "Users", id]), params.to_dict())
            )
        )

    # Modify an existing user in TravelPerk.
    def modify(
        self, id: int, username: str, active: bool, given_name: str, family_name: str
    ) -> ModifyUserRequest:
        name = NameInputParams(given_name, family_name)
        return ModifyUserRequest(id, self.travelperk, username, active, name)

    # Get all genders.
    def genders(self) -> List[str]:
        return [gender.value for gender in Gender]

    # Get all languages.
    def languages(self) -> List[str]:
        return [language.value for language in Language]
