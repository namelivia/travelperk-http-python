import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.trips.trips import Trips


class TestTrips:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.trips = Trips(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_trips_stub(self, trips_page):
        assert trips_page.total == 2
        assert trips_page.offset == 0
        assert trips_page.limit == 10
        assert len(trips_page.trips) == 2
        assert trips_page.trips[0].id == "172"
        assert trips_page.trips[0].trip_name == "The Great Voyage"
        assert trips_page.trips[0].start == "2020-11-20T00:00:00"
        assert trips_page.trips[0].end == "2020-11-25T00:00:00"
        assert trips_page.trips[0].status == "booked"
        assert trips_page.trips[0].modified == "2020-09-16T07:08:06.290253+00:00"
        assert trips_page.trips[1].id == "205"
        assert trips_page.trips[1].trip_name == "Road trip Barcelona"
        assert trips_page.trips[1].start == "2020-09-25T10:00:00+00:00"
        assert trips_page.trips[1].end == "2020-09-26T10:00:00+00:00"
        assert trips_page.trips[1].status == "booked"
        assert trips_page.trips[1].modified == "2020-09-14T12:55:06.720754+00:00"

    def test_getting_all_trips_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("trips.json")
        trips = self.trips.query().set_offset(5).set_limit(10).get()
        self.assert_equals_trips_stub(trips)

    # TODO: Implement this
    def test_getting_statuses(self):
        pass
