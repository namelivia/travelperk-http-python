import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.scim.users import Users
from travelperk_http_python.scim.users_input_params import UsersInputParams


class TestSCIMUsers:
    def setup_method(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.users = Users(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def test_getting_all_users_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("scim_users.json")
        users = self.users.query().set_count(5).set_start_index(3).get()
        self.travelperk.get.assert_called_once_with("scim/Users?count=5&startIndex=3")
        assert users.total_results == 2
        assert users.items_per_page == 2
        assert users.start_index == 1
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == users.resources[0].schemas
        assert users.resources[0].name.given_name == "Marlen"
        assert users.resources[0].name.family_name == "Col"
        assert users.resources[0].name.middle_name == ""
        assert users.resources[0].name.honorific_prefix == ""
        assert users.resources[0].locale == "en"
        assert users.resources[0].preferred_language == "en"
        assert users.resources[0].title == "Manager"
        assert users.resources[0].external_id == "123455667"
        assert users.resources[0].id == "29"
        assert users.resources[0].groups == []
        assert users.resources[0].active is True
        assert users.resources[0].user_name == "marlen.col@mycompany.com"
        assert len(users.resources[0].phone_numbers) == 1
        assert users.resources[0].phone_numbers[0].value == "+34 1234567"
        assert users.resources[0].phone_numbers[0].type == "work"
        assert users.resources[0].meta.resource_type == "User"
        assert users.resources[0].meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert (
            users.resources[0].meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        )
        assert (
            users.resources[0].meta.location
            == "http://app.travelperk.com/api/v2/scim/Users/29"
        )
        assert users.resources[0].enterprise_extension.cost_center == "Marketing"
        assert users.resources[0].enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == users.resources[0].enterprise_extension.manager.ref
        )
        assert (
            users.resources[0].enterprise_extension.manager.display_name
            == "Jack Jackson"
        )
        assert users.resources[0].travelperk_extension.gender == "M"
        assert users.resources[0].travelperk_extension.date_of_birth == "1980-02-02"
        assert (
            users.resources[0].travelperk_extension.travel_policy
            == "Marketing travel policy"
        )
        assert len(users.resources[0].travelperk_extension.invoice_profiles) == 1
        assert (
            users.resources[0].travelperk_extension.invoice_profiles[0].value
            == "My Company Ltd"
        )

    def test_getting_all_users_non_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("scim_users.json")
        users = self.users.query().get()
        self.travelperk.get.assert_called_once_with("scim/Users?")
        assert users.total_results == 2
        assert users.items_per_page == 2
        assert users.start_index == 1
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == users.resources[0].schemas
        assert users.resources[0].name.given_name == "Marlen"
        assert users.resources[0].name.family_name == "Col"
        assert users.resources[0].name.middle_name == ""
        assert users.resources[0].name.honorific_prefix == ""
        assert users.resources[0].locale == "en"
        assert users.resources[0].preferred_language == "en"
        assert users.resources[0].title == "Manager"
        assert users.resources[0].external_id == "123455667"
        assert users.resources[0].id == "29"
        assert users.resources[0].groups == []
        assert users.resources[0].active is True
        assert users.resources[0].user_name == "marlen.col@mycompany.com"
        assert len(users.resources[0].phone_numbers) == 1
        assert users.resources[0].phone_numbers[0].value == "+34 1234567"
        assert users.resources[0].phone_numbers[0].type == "work"
        assert users.resources[0].meta.resource_type == "User"
        assert users.resources[0].meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert (
            users.resources[0].meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        )
        assert (
            users.resources[0].meta.location
            == "http://app.travelperk.com/api/v2/scim/Users/29"
        )
        assert users.resources[0].enterprise_extension.cost_center == "Marketing"
        assert users.resources[0].enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == users.resources[0].enterprise_extension.manager.ref
        )
        assert (
            users.resources[0].enterprise_extension.manager.display_name
            == "Jack Jackson"
        )
        assert users.resources[0].travelperk_extension.gender == "M"
        assert users.resources[0].travelperk_extension.date_of_birth == "1980-02-02"
        assert (
            users.resources[0].travelperk_extension.travel_policy
            == "Marketing travel policy"
        )
        assert len(users.resources[0].travelperk_extension.invoice_profiles) == 1
        assert (
            users.resources[0].travelperk_extension.invoice_profiles[0].value
            == "My Company Ltd"
        )
        assert (
            users.resources[0].travelperk_extension.emergency_contact.name
            == "Jane Goodie"
        )
        assert (
            users.resources[0].travelperk_extension.emergency_contact.phone
            == "+34 9874637"
        )
        assert (
            users.resources[0].travelperk_extension.emergency_contact.name
            == "Jane Goodie"
        )
        assert (
            users.resources[0].travelperk_extension.emergency_contact.phone
            == "+34 9874637"
        )

    def test_getting_a_user_detail(self):
        self.travelperk.get.return_value = self.get_stub_contents("scim_user.json")
        user = self.users.get(1)
        self.travelperk.get.assert_called_once_with("scim/Users/1")
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == user.schemas
        assert user.name.given_name == "Marlen"
        assert user.name.family_name == "Col"
        assert user.name.middle_name == ""
        assert user.name.honorific_prefix == ""
        assert user.locale == "en"
        assert user.preferred_language == "en"
        assert user.title == "Manager"
        assert user.external_id == "123455667"
        assert user.id == "29"
        assert user.groups == []
        assert user.active is True
        assert user.user_name == "marlen.col@mycompany.com"
        assert len(user.phone_numbers) == 1
        assert user.phone_numbers[0].value == "+34 1234567"
        assert user.phone_numbers[0].type == "work"
        assert user.meta.resource_type == "User"
        assert user.meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.location == "http://app.travelperk.com/api/v2/scim/Users/29"
        assert user.enterprise_extension.cost_center == "Marketing"
        assert user.enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == user.enterprise_extension.manager.ref
        )
        assert user.enterprise_extension.manager.display_name == "Jack Jackson"
        assert user.travelperk_extension.gender == "M"
        assert user.travelperk_extension.date_of_birth == "1980-02-02"
        assert user.travelperk_extension.travel_policy == "Marketing travel policy"
        assert len(user.travelperk_extension.invoice_profiles) == 1
        assert user.travelperk_extension.invoice_profiles[0].value == "My Company Ltd"
        assert user.travelperk_extension.emergency_contact.name == "Jane Goodie"
        assert user.travelperk_extension.emergency_contact.phone == "+34 9874637"

    def test_deleting_a_user(self):
        self.travelperk.delete.return_value = "userDeleted"
        assert self.users.delete(1) == "userDeleted"
        self.travelperk.delete.assert_called_once_with("scim/Users/1")

    def test_making_and_saving_a_user(self):
        self.travelperk.post.return_value = self.get_stub_contents("scim_user.json")
        user = (
            self.users.make(
                "testuser@test.com",
                True,
                "Test",
                "User",
            )
            .set_honorific_prefix("Dr")
            .set_locale("en")
            .set_title("manager")
            .save()
        )
        self.travelperk.post.assert_called_once_with(
            "scim/Users",
            {
                "userName": "testuser@test.com",
                "name": {
                    "givenName": "Test",
                    "familyName": "User",
                    "honorificPrefix": "Dr",
                },
                "active": True,
                "locale": "en",
                "title": "manager",
            },
        )
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == user.schemas
        assert user.name.given_name == "Marlen"
        assert user.name.family_name == "Col"
        assert user.name.middle_name == ""
        assert user.name.honorific_prefix == ""
        assert user.locale == "en"
        assert user.preferred_language == "en"
        assert user.title == "Manager"
        assert user.external_id == "123455667"
        assert user.id == "29"
        assert user.groups == []
        assert user.active is True
        assert user.user_name == "marlen.col@mycompany.com"
        assert len(user.phone_numbers) == 1
        assert user.phone_numbers[0].value == "+34 1234567"
        assert user.phone_numbers[0].type == "work"
        assert user.meta.resource_type == "User"
        assert user.meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.location == "http://app.travelperk.com/api/v2/scim/Users/29"
        assert user.enterprise_extension.cost_center == "Marketing"
        assert user.enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == user.enterprise_extension.manager.ref
        )
        assert user.enterprise_extension.manager.display_name == "Jack Jackson"
        assert user.travelperk_extension.gender == "M"
        assert user.travelperk_extension.date_of_birth == "1980-02-02"
        assert user.travelperk_extension.travel_policy == "Marketing travel policy"
        assert len(user.travelperk_extension.invoice_profiles) == 1
        assert user.travelperk_extension.invoice_profiles[0].value == "My Company Ltd"
        assert user.travelperk_extension.emergency_contact.name == "Jane Goodie"
        assert user.travelperk_extension.emergency_contact.phone == "+34 9874637"

    def test_creating_a_user(self):
        self.travelperk.post.return_value = self.get_stub_contents("scim_user.json")
        user = self.users.create(
            "testuser@test.com",
            True,
            "Test",
            "User",
        )
        self.travelperk.post.assert_called_once_with(
            "scim/Users",
            {
                "userName": "testuser@test.com",
                "name": {
                    "givenName": "Test",
                    "familyName": "User",
                },
                "active": True,
            },
        )
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == user.schemas
        assert user.name.given_name == "Marlen"
        assert user.name.family_name == "Col"
        assert user.name.middle_name == ""
        assert user.name.honorific_prefix == ""
        assert user.locale == "en"
        assert user.preferred_language == "en"
        assert user.title == "Manager"
        assert user.external_id == "123455667"
        assert user.id == "29"
        assert user.groups == []
        assert user.active is True
        assert user.user_name == "marlen.col@mycompany.com"
        assert len(user.phone_numbers) == 1
        assert user.phone_numbers[0].value == "+34 1234567"
        assert user.phone_numbers[0].type == "work"
        assert user.meta.resource_type == "User"
        assert user.meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.location == "http://app.travelperk.com/api/v2/scim/Users/29"
        assert user.enterprise_extension.cost_center == "Marketing"
        assert user.enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == user.enterprise_extension.manager.ref
        )
        assert user.enterprise_extension.manager.display_name == "Jack Jackson"
        assert user.travelperk_extension.gender == "M"
        assert user.travelperk_extension.date_of_birth == "1980-02-02"
        assert user.travelperk_extension.travel_policy == "Marketing travel policy"
        assert len(user.travelperk_extension.invoice_profiles) == 1
        assert user.travelperk_extension.invoice_profiles[0].value == "My Company Ltd"
        assert user.travelperk_extension.emergency_contact.name == "Jane Goodie"
        assert user.travelperk_extension.emergency_contact.phone == "+34 9874637"

    def test_updating_a_user(self):
        pass
        # TODO: Rewrite this test
        # params = Mock(spec=UpdateUserInputParams)
        # user_id = 1
        # $this.expectException(NotImplementedException::class)
        # $this.expectExceptionMessage('https://github.com/namelivia/travelperk-http-php/issues/7')
        # self.users.update(user_id, params)

    def test_replacing_a_user(self):
        self.travelperk.put.return_value = self.get_stub_contents("scim_user.json")
        user_id = 1
        user = (
            self.users.modify(
                user_id,
                "testuser@test.com",
                True,
                "Test",
                "User",
            )
            .set_honorific_prefix("Dr")
            .set_title("manager")
            .save()
        )
        self.travelperk.put.assert_called_once_with(
            "scim/Users/1",
            {
                "userName": "testuser@test.com",
                "name": {
                    "givenName": "Test",
                    "familyName": "User",
                    "honorificPrefix": "Dr",
                },
                "active": True,
                "title": "manager",
            },
        )
        assert [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
        ] == user.schemas
        assert user.name.given_name == "Marlen"
        assert user.name.family_name == "Col"
        assert user.name.middle_name == ""
        assert user.name.honorific_prefix == ""
        assert user.locale == "en"
        assert user.preferred_language == "en"
        assert user.title == "Manager"
        assert user.external_id == "123455667"
        assert user.id == "29"
        assert user.groups == []
        assert user.active is True
        assert user.user_name == "marlen.col@mycompany.com"
        assert len(user.phone_numbers) == 1
        assert user.phone_numbers[0].value == "+34 1234567"
        assert user.phone_numbers[0].type == "work"
        assert user.meta.resource_type == "User"
        assert user.meta.created == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.last_modified == "2020-04-01T22:24:44.137082+00:00"
        assert user.meta.location == "http://app.travelperk.com/api/v2/scim/Users/29"
        assert user.enterprise_extension.cost_center == "Marketing"
        assert user.enterprise_extension.manager.value == "123"
        assert (
            "https://app.travelperk.com/api/v2/scim/Users/123/"
            == user.enterprise_extension.manager.ref
        )
        assert user.enterprise_extension.manager.display_name == "Jack Jackson"
        assert user.travelperk_extension.gender == "M"
        assert user.travelperk_extension.date_of_birth == "1980-02-02"
        assert user.travelperk_extension.travel_policy == "Marketing travel policy"
        assert len(user.travelperk_extension.invoice_profiles) == 1
        assert user.travelperk_extension.invoice_profiles[0].value == "My Company Ltd"
        assert user.travelperk_extension.emergency_contact.name == "Jane Goodie"
        assert user.travelperk_extension.emergency_contact.phone == "+34 9874637"

    def test_getting_all_genders(self):
        assert self.users.genders() == ["M", "F"]

    def test_getting_all_languages(self):
        assert self.users.languages() == ["en", "fr", "de", "es"]
