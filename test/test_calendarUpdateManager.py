#!/usr/bin/env python3
import os

import pytest
import requests

from api.models.CalendarUpdateManager import CalendarUpdateManager
from api.models.UserCalendar import CALENDAR_MANAGER

class TestUpdateManager:
    """Test the calendar update manager
    """
    calendarURL = 'https://gist.githubusercontent.com/ThoreKr/1b5b66a48fca07f568f362be4221202a/raw/82cc5301a6201dfb7ef972c8349a4a4412f88d07/demo.ics'
    CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')

    @pytest.fixture(scope='class')
    def demoCalendar(self):
        """Non mocked request to get the demo calendar
        """
        return requests.get(self.calendarURL).text

    @pytest.fixture(scope='function')
    def testCalendar(self, requests_mock, demoCalendar):
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/DEMO', status_code=200, json={'calendarURL': self.calendarURL})
        requests_mock.get(self.calendarURL, text=demoCalendar)

        calendar = CALENDAR_MANAGER.getCalendar('DEMO')
        calendar.url = self.calendarURL
        calendar.update()
        return CALENDAR_MANAGER

    def test_updateManager(self, testCalendar, requests_mock, demoCalendar):
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/DEMO', status_code=200, json={'calendarURL': self.calendarURL})
        requests_mock.get(self.calendarURL, text=demoCalendar)

        updateManager = CalendarUpdateManager(calendarManager=testCalendar)
        assert True
