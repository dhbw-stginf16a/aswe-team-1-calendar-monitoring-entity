#!/usr/bin/env python3

import logging
from datetime import datetime, timedelta

import requests
from ics import Calendar

from api.models.prefstore import getCalendarURL


logger = logging.getLogger(__name__)


class UserCalendar:
    """Object for a calendar from a specific user
    """

    def __init__(self, url):
        self.url = url
        self.calendar = Calendar(requests.get(url).text)

    def update(self):
        """Updates the current calendar object
        """
        self.calendar = Calendar(requests.get(self.url).text)

    def getEventsDay(self, date: datetime):
        eventList = list()
        for event in self.calendar.events:
            if event.begin.date() == date.date():
                logger.debug('Found event for given date')
                eventList.append(event)
        return eventList

    def getEventsTimeRange(self, startDate: datetime, endDate: datetime):
        delta = endDate - startDate
        logger.debug(delta)
        eventList = list()
        for i in range(delta.days + 1):
            eventList.extend(self.getEventsDay(startDate + timedelta(i)))

        return eventList

class UserCalendarManager:
    """Manages all calendar objects to get, destroy and instantiate them
    """

    def __init__(self):
        self.calendars = {}

    def getCalendar(self, calendarName):
        calendar = self.calendars.setdefault(calendarName, UserCalendar(getCalendarURL(calendarName)))
        return calendar

    def getCalendars(self):
        # Return a copy to avoid changing size during iteration in the update worker
        return self.calendars.copy()

CALENDAR_MANAGER = UserCalendarManager()
