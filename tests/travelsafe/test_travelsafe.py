import datetime
import os
import json
from mock import Mock
from freezegun import freeze_time
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_http_python.travelsafe.travelsafe import TravelSafe


class TestTravelSafe:
    def setup(self):
        self.travelperk = Mock(spec=TravelPerk)
        self.travelsafe = TravelSafe(self.travelperk)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "../stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    @freeze_time("2019-03-21")
    def test_getting_travel_restrictions(self):
        self.travelperk.get.return_value = self.get_stub_contents("restriction.json")
        restriction = self.travelsafe.travel_restrictions(
            "ES", "FR", "country_code", "country_code", datetime.date.today()
        )
        self.travelperk.get.assert_called_once_with(
            "travelsafe/restrictions?origin=ES&destination=FR&origin_type=country_code&destination_type=country_code&date=2019-03-21"
        )
        assert restriction.id == "e7975c43-b098-4530-ad3e-59615b8572ac"
        assert restriction.origin.name == "France"
        assert restriction.origin.type == "country"
        assert restriction.origin.country_code == "FR"
        assert restriction.destination.name == "Spain"
        assert restriction.destination.type == "country"
        assert restriction.destination.country_code == "ES"
        assert restriction.authorization_status == "restricted"
        assert restriction.summary == "Travelling from France to Spain is restricted"
        assert restriction.details == "Only business related travel is allowed."
        assert restriction.start_date == "2020-10-16"
        assert restriction.end_date is None
        assert restriction.updated_at == "2020-09-16T14:54:59.944581+00:00"
        assert len(restriction.requirements) == 1
        assert restriction.requirements[0].category.id == "quarantine"
        assert restriction.requirements[0].category.name == "Quarantine"
        assert restriction.requirements[0].sub_category.id == "quarantine_required"
        assert restriction.requirements[0].sub_category.name == "Quarantine required"
        assert (
            restriction.requirements[0].summary
            == "Travelers are required to quarantine for 14 days prior or after entering this destination"
        )
        assert (
            restriction.requirements[0].details
            == "Travelers arriving into Spain are required to go into quarantine"
        )
        assert restriction.requirements[0].start_date == "2020-10-02"
        assert restriction.requirements[0].end_date is None
        assert len(restriction.requirements[0].documents) == 1
        assert restriction.requirements[0].documents[0].name == "FCS form"
        assert (
            restriction.requirements[0].documents[0].document_url
            == "https://www.spth.gob.es/create"
        )
        assert (
            restriction.requirements[0].documents[0].download_url
            == "https://www.spth.gob.es/download.pdf"
        )

    def test_getting_local_summary(self):
        self.travelperk.get.return_value = self.get_stub_contents("summary.json")
        summary = self.travelsafe.local_summary("ES", "country_code")
        self.travelperk.get.assert_called_once_with(
            "travelsafe/guidelines?location_type=country_code&location=ES"
        )
        assert summary.id == "872aca1b-04ca-47d2-83d8-493b4c7b6148"
        assert (
            summary.summary
            == "While traveling in Spain you will be required to follow the guidelines introduced by the local government. These regulations are based on risk levels and aimed at improving your safety."
        )
        assert summary.details == ""
        assert summary.risk_level.id == "high"
        assert summary.risk_level.name == "High"
        assert summary.risk_level.details == "Covid cases are multiplying"
        assert summary.location.name == "Spain"
        assert summary.location.type == "country"
        assert summary.location.country_code == "ES"
        assert summary.updated_at == "2020-10-19T10:08:53.777Z"
        assert len(summary.guidelines) == 1
        assert summary.guidelines[0].category.id == "use_of_mask"
        assert summary.guidelines[0].category.name == "Use of masks"
        assert summary.guidelines[0].sub_category.id == "required"
        assert summary.guidelines[0].sub_category.name == "Required"
        assert summary.guidelines[0].summary == "Use of masks is required"
        assert (
            summary.guidelines[0].details
            == "Use of masks in all the public areas is required, including open spaces. You might face fines up to €3000 if stopped by the police without mask."
        )
        assert summary.guidelines[0].severity == "1/3"
        assert summary.info_source.name == "Spain Travel Health"
        assert summary.info_source.url == "https://www.spth.gob.es/"

    def test_airline_safety_measures(self):
        self.travelperk.get.return_value = self.get_stub_contents(
            "airline_measures.json"
        )
        safety_measure = self.travelsafe.airline_safety_measures("iata")
        self.travelperk.get.assert_called_once_with(
            "travelsafe/airline_safety_measures?iata_code=iata"
        )
        assert safety_measure.airline.name == "Lufthansa"
        assert safety_measure.airline.iata_code == "LH"
        assert len(safety_measure.safety_measures) == 1
        assert (
            safety_measure.safety_measures[0].category.id
            == "boarding_or_dissembarking_measurements"
        )
        assert (
            safety_measure.safety_measures[0].category.name
            == "New boarding and disembarking measures"
        )
        assert safety_measure.safety_measures[0].sub_category.id == "true"
        assert safety_measure.safety_measures[0].sub_category.name == "true"
        assert (
            safety_measure.safety_measures[0].details
            == "Travelers should wait until their boarding group is called before using the automatic gates to board the aircraft. Disinfectant wipes will also be provided to passengers for the purpose of cleaning the surfaces in and around their seats."
        )
        assert (
            safety_measure.safety_measures[0].summary
            == "To help passengers can keep a safe distance from one another."
        )
        assert safety_measure.info_source.name == "Lufthansa' info source"
        assert (
            safety_measure.info_source.url
            == "https://www.lufthansa.com/de/en/protection-measures"
        )
        assert safety_measure.updated_at == "2020-10-19T12:14:42.041298+00:00"

    def test_getting_all_location_types(self):
        assert self.travelsafe.location_types() == ["country_code", "iata_code"]
