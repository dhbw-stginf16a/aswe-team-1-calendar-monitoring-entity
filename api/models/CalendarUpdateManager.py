#!/usr/bin/env python3

import logging
import datetime
import threading
import time

from api.models.UserCalendar import CALENDAR_MANAGER
from api.models.utils import eventToJSON

logger = logging.getLogger(__name__)

class CalendarUpdateManager:
    """This is a manager to constantly iterate over all calendars and update them
    """
    notificationBlockList = {}

    def __init__(self, calendarManager=CALENDAR_MANAGER, interval=3600):
        self.calendarManager = calendarManager
        self.interval = interval

        logger.info('Creating update thread')
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread

        logger.info('Starting update thread')
        thread.start()                                  # Start the execution


    def sendNotifications(self, notificationList):
        """Sends out the events of a new calendar event
        """
        for calendar, events in notificationList.items():
            logger.info('Calendar: %s', calendar)
            for event in events:
                logger.info('Event: %s', event)

    def generateNotificationList(self):
        """Genereates a list of users and events they need to be updated about
        """
        notificationList = {}
        for calendarName, calendar in self.calendarManager.getCalendars().items():
            calendar.update()
            # Use this knowlege about new events later for something cool.

            # get a list of all events today and save them into a list (so we can deduplicate)
            events = calendar.getEventsDay(datetime.datetime.today())

            self.notificationBlockList.setdefault(calendarName, list())
            for event in events:
                # Detect events not already notified
                if event.uid not in self.notificationBlockList[calendarName]:
                    # Creates a small overhead but the user then never appears in the list when there is no event
                    notificationList.setdefault(calendarName, list())
                    notificationList[calendarName].append(eventToJSON(event))
                    self.notificationBlockList[calendarName].append(event.uid)

        return notificationList

    def run(self):
        """The threads entrypoint
        """
        while True:
            logger.debug('Running update')
            notificationList = self.generateNotificationList()

            self.sendNotifications(notificationList)
            time.sleep(self.interval)
