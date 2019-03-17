#!/usr/bin/env python3

import pytest

from api.models.CalendarUpdateManager import CalendarUpdateManager
from api.models.UserCalendar import CALENDAR_MANAGER

class TestUpdateManager:
    """Test the calendar update manager
    """
    @pytest.fixture(scope='class')
    def testCalendar(self):
        calendar = CALENDAR_MANAGER.getCalendar('NASA')
        calendar.url = 'https://gist.githubusercontent.com/ThoreKr/1b5b66a48fca07f568f362be4221202a/raw/82cc5301a6201dfb7ef972c8349a4a4412f88d07/demo.ics'
        calendar.update()
        return CALENDAR_MANAGER

    def test_updateManager(self, testCalendar):
        updateManager = CalendarUpdateManager(calendarManager=testCalendar)
        assert True
