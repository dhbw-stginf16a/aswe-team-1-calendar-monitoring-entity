from datetime import datetime
import pytest

import requests

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestRequest(TestConnexion):
    """A test to get events from the calendar api
    """
    nasaURL = 'http://www.nasa.gov/templateimages/redesign/calendar/iCal/nasa_calendar.ics'

    @pytest.fixture(scope='class')
    def nasaCalendar(self):
        """A non-mocked request to get the nasa ics
        """
        return requests.get(self.nasaURL).text

    def test_getEventsDay(self, client, requests_mock, nasaCalendar):
        print(self.CENTRAL_NODE_BASE_URL)
        request = {
            'type': 'event_date',
            'payload': {
                'user': 'AntonHynkel',
                'date': '2007-11-01'
            }
        }
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/test', status_code=200, json={'calendarURL': self.nasaURL})
        requests_mock.get(self.nasaURL, text=nasaCalendar)
        response = client.post('/api/v1/request', json=request)

        assert response.status_code == 200

    def test_getEventsTimerange(self, client, requests_mock, nasaCalendar):
        request = {
            'type': 'event_timerange',
            'payload': {
                'user': 'AntonHynkel',
                'startDate': '2007-01-01',
                'endDate':  '2007-12-31'
            }
        }
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/test', status_code=200, json={'calendarURL': self.nasaURL})
        requests_mock.get(self.nasaURL, text=nasaCalendar)
        response = client.post('/api/v1/request', json=request)

        assert response.status_code == 200
