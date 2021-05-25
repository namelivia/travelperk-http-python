import os
import json
from mock import Mock
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.trips.bookings import Bookings


class TestBookings:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.bookings = Bookings(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_bookings_stub(self, bookings_page):
        assert bookings_page.total == 4
        assert bookings_page.offset == 0
        assert bookings_page.limit == 10
        assert len(bookings_page.bookings) == 4

        assert bookings_page.bookings[0].id == "71"
        assert bookings_page.bookings[0].start == "2021-03-06T00:00:00+00:00"
        assert bookings_page.bookings[0].end == "2021-03-07T00:00:00+00:00"
        assert bookings_page.bookings[0].type == "hotel"
        assert bookings_page.bookings[0].status == "ticketed"
        assert bookings_page.bookings[0].modified == "2021-01-04T11:11:20.714987+00:00"
        assert bookings_page.bookings[0].trip_id == "51"
        assert len(bookings_page.bookings[0].references) == 1
        assert bookings_page.bookings[0].references[0].type == "confirmation_number"
        assert bookings_page.bookings[0].references[0].value == "4636"
        assert bookings_page.bookings[0].location.latitude == "59.5468062"
        assert bookings_page.bookings[0].location.longitude == "113.9913155"
        assert bookings_page.bookings[0].location.iata_code is None
        assert bookings_page.bookings[0].legs is None

        assert bookings_page.bookings[1].id == "73"
        assert bookings_page.bookings[1].start == "2021-03-06T00:00:00+00:00"
        assert bookings_page.bookings[1].end == "2021-03-09T00:00:00+00:00"
        assert bookings_page.bookings[1].type == "car"
        assert bookings_page.bookings[1].status == "ticketed"
        assert bookings_page.bookings[1].modified == "2021-01-03T11:11:20.714987+00:00"
        assert bookings_page.bookings[1].trip_id == "51"
        assert len(bookings_page.bookings[1].references) == 2
        assert bookings_page.bookings[1].references[0].type == "voucher_code"
        assert bookings_page.bookings[1].references[0].value == "voucher_12"
        assert bookings_page.bookings[1].references[1].type == "confirmation_number"
        assert bookings_page.bookings[1].references[1].value == "cn_17"
        assert bookings_page.bookings[1].location.latitude == "-56.0"
        assert bookings_page.bookings[1].location.longitude == "-62.0"
        assert bookings_page.bookings[1].location.iata_code is None

        assert bookings_page.bookings[2].id == "70"
        assert bookings_page.bookings[2].start == "2021-03-06T00:00:00+00:00"
        assert bookings_page.bookings[2].end == "2021-03-07T00:00:00+00:00"
        assert bookings_page.bookings[2].type == "flight"
        assert bookings_page.bookings[2].status == "ticketed"
        assert bookings_page.bookings[2].modified == "2021-01-02T11:11:20.714987+00:00"
        assert bookings_page.bookings[2].trip_id == "51"
        assert len(bookings_page.bookings[2].references) == 1
        assert bookings_page.bookings[2].references[0].type == "PNR"
        assert bookings_page.bookings[2].references[0].value == "HNTCEBSMPO"
        assert bookings_page.bookings[2].location is None
        assert len(bookings_page.bookings[2].legs) == 2
        assert len(bookings_page.bookings[2].legs[0].segments) == 2
        assert len(bookings_page.bookings[2].legs[1].segments) == 2
        assert (
            bookings_page.bookings[2].legs[0].segments[0].origin.location.latitude
            == "85.5975436"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].origin.location.longitude
            == "18.7959996"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].origin.location.iata_code
            == "UYM"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].origin.time
            == "2021-03-06T00:00:00+01:00"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].destination.location.latitude
            == "-54.3854772"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].destination.location.longitude
            == "81.6402173"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].destination.location.iata_code
            == "EKD"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[0].destination.time
            == "2021-03-07T12:00:00+01:00"
        )
        assert bookings_page.bookings[2].legs[0].segments[0].external_id == "XX1234"
        assert (
            bookings_page.bookings[2].legs[0].segments[1].origin.location.latitude
            == "67.1291014"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].origin.location.longitude
            == "21.1347543"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].origin.location.iata_code
            == "IWP"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].origin.time
            == "2021-03-08T00:00:00+01:00"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].destination.location.latitude
            == "8.6677113"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].destination.location.longitude
            == "-13.9691879"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].destination.location.iata_code
            == "TMQ"
        )
        assert (
            bookings_page.bookings[2].legs[0].segments[1].destination.time
            == "2021-03-09T12:00:00+01:00"
        )
        assert bookings_page.bookings[2].legs[0].segments[1].external_id == "XX1234"
        assert (
            bookings_page.bookings[2].legs[1].segments[0].origin.location.latitude
            == "23.5841460"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].origin.location.longitude
            == "-141.9148137"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].origin.location.iata_code
            == "UJH"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].origin.time
            == "2021-03-10T12:00:00+01:00"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].destination.location.latitude
            == "-6.0933315"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].destination.location.longitude
            == "-7.6775088"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].destination.location.iata_code
            == "ZVO"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[0].destination.time
            == "2021-03-11T00:00:00+01:00"
        )
        assert bookings_page.bookings[2].legs[1].segments[0].external_id == "XX1234"
        assert (
            bookings_page.bookings[2].legs[1].segments[1].origin.location.latitude
            == "78.4132615"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].origin.location.longitude
            == "-156.7342795"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].origin.location.iata_code
            == "OJR"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].origin.time
            == "2021-03-12T12:00:00+01:00"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].destination.location.latitude
            == "-44.6617225"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].destination.location.longitude
            == "163.2773819"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].destination.location.iata_code
            == "YNX"
        )
        assert (
            bookings_page.bookings[2].legs[1].segments[1].destination.time
            == "2021-03-13T00:00:00+01:00"
        )
        assert bookings_page.bookings[2].legs[1].segments[1].external_id == "XX1234"

        assert bookings_page.bookings[3].id == "72"
        assert bookings_page.bookings[3].start == "2021-03-06T00:00:00+00:00"
        assert bookings_page.bookings[3].end == "2021-03-07T00:00:00+00:00"
        assert bookings_page.bookings[3].type == "train"
        assert bookings_page.bookings[3].status == "ticketed"
        assert bookings_page.bookings[3].modified == "2021-01-01T11:11:20.714987+00:00"
        assert bookings_page.bookings[3].trip_id == "51"
        assert len(bookings_page.bookings[3].references) == 1
        assert (
            bookings_page.bookings[3].references[0].type
            == "ticket_collection_reference"
        )
        assert bookings_page.bookings[3].references[0].value == "PMXFIQ"
        assert bookings_page.bookings[3].location is None
        assert len(bookings_page.bookings[3].legs) == 1
        assert len(bookings_page.bookings[3].legs[0].segments) == 1
        assert (
            bookings_page.bookings[3].legs[0].segments[0].origin.location.latitude
            == "-73.000000000"
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].origin.location.longitude
            == "-26.000000000"
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].origin.location.iata_code
            is None
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].origin.time
            == "2021-03-06T00:00:00+00:00"
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].destination.location.latitude
            == "-30.000000000"
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].destination.location.longitude
            == "83.000000000"
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].destination.location.iata_code
            is None
        )
        assert (
            bookings_page.bookings[3].legs[0].segments[0].destination.time
            == "2021-03-09T00:00:00+00:00"
        )
        assert bookings_page.bookings[3].legs[0].segments[0].external_id == "XX1234"

    def test_getting_all_bookings_with_params(self):
        self.travelperk.get.return_value = self.get_stub_contents("bookings.json")
        bookings = self.bookings.query().set_offset(5).set_limit(10).get()
        self.travelperk.get.assert_called_once_with("bookings?offset=5&limit=10")
        self.assert_equals_bookings_stub(bookings)

    # TODO: Implement this
    def test_getting_statuses(self):
        pass

    # TODO: Implement this
    def test_getting_types(self):
        pass
