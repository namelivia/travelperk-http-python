import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.cost_centers.cost_centers import CostCenters


class TestCostCenters:
    def setup_method(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.cost_centers = CostCenters(self.travelperk)

    def assert_equals_cost_centers_stub(self, cost_centers_page):
        assert cost_centers_page.offset == 0
        assert cost_centers_page.limit == 10
        assert len(cost_centers_page.cost_centers) == 1
        assert cost_centers_page.cost_centers[0].id == 2
        assert cost_centers_page.cost_centers[0].name == "Test Cost Center 2"
        assert cost_centers_page.cost_centers[0].count_users == 0

    def assert_equals_cost_center_stub(self, cost_center):
        assert cost_center.id == 1
        assert cost_center.name == "iloveorange"
        assert cost_center.archived is True
        assert len(cost_center.users) == 1
        assert cost_center.users[0].first_name == "Name"
        assert cost_center.users[0].last_name == "Lastname"
        assert cost_center.users[0].email == "email@email.com"
        assert cost_center.users[0].id == 1
        assert cost_center.users[0].phone is None
        assert cost_center.users[0].profile_picture is None
        assert cost_center.count_users == 1

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def test_getting_all_cost_centers(self):
        self.travelperk.get.return_value = self.get_stub_contents("cost_centers.json")
        cost_centers = self.cost_centers.all()
        self.travelperk.get.assert_called_once_with("cost_centers")
        self.assert_equals_cost_centers_stub(cost_centers)

    def test_getting_a_cost_center_details(self):
        cost_center_id = "1"
        self.travelperk.get.return_value = self.get_stub_contents("cost_center.json")
        cost_center = self.cost_centers.get(cost_center_id)
        self.travelperk.get.assert_called_once_with("cost_centers/1")
        self.assert_equals_cost_center_stub(cost_center)

    def test_creating_a_cost_center(self):
        self.travelperk.post.return_value = self.get_stub_contents("cost_center.json")
        cost_center = self.cost_centers.create("test")
        self.travelperk.post.assert_called_once_with("cost_centers", {"name": "test"})
        self.assert_equals_cost_center_stub(cost_center)

    def test_modifying_a_cost_center(self):
        cost_center_id = 1
        self.travelperk.patch.return_value = self.get_stub_contents("cost_center.json")
        cost_center = (
            self.cost_centers.modify(cost_center_id)
            .set_name("newName")
            .set_archive(False)
            .save()
        )
        self.travelperk.patch.assert_called_once_with(
            "cost_centers/1", {"name": "newName", "archive": False}
        )
        self.assert_equals_cost_center_stub(cost_center)

    def test_bulk_updating_cost_centers(self):
        self.travelperk.patch.return_value = self.get_stub_contents("bulk_update.json")
        result = (
            self.cost_centers.bulk_update()
            .set_ids([1, 2, 3, 4])
            .set_archive(False)
            .save()
        )
        self.travelperk.patch.assert_called_once_with(
            "cost_centers/bulk_update", {"id_list": [1, 2, 3, 4], "archive": False}
        )
        assert result.updated_count == 1
