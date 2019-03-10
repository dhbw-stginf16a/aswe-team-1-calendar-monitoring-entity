from datetime import datetime
import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestRequest(TestConnexion):
    """A test to get events from the calendar api
    """

    def test_getEventsDay(self, client):
        request = {
            'type': 'event_date',
            'payload': {
                'user': 'AntonHynkel',
                'date': '2007-11-01'
            }
        }

        response = client.post('api/v1/request', json=request)

        assert response.status_code == 200
        print(response.get_json())

    def test_getEventsTimerange(self, client):
        request = {
            'type': 'event_timerange',
            'payload': {
                'user': 'AntonHynkel',
                'startDate': '2007-01-01',
                'endDate':  '2007-12-31'
            }
        }

        response = client.post('api/v1/request', json=request)

        assert response.status_code == 200
        print(response.get_json())
