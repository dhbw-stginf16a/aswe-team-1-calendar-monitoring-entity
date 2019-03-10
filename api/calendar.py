#!/usr/bin/env python3

import logging

import dateutil.parser

from api.models.UserCalendar import CALENDAR_MANAGER
from api.models.utils import eventToJSON

logger = logging.getLogger(__name__)


def getCalendar(body):
    calendar = CALENDAR_MANAGER.getCalendar(body['payload']['user'])
    if body['type'] == 'event_date':
        date = dateutil.parser.parse(body['payload']['date'])
        logger.debug(date)
        eventList = calendar.getEventsDay(date)
    elif body['type'] == 'event_timerange':
        startDate = dateutil.parser.parse(body['payload']['startDate'])
        endDate = dateutil.parser.parse(body['payload']['endDate'])
        eventList = calendar.getEventsTimeRange(startDate, endDate)

    events = [eventToJSON(event) for event in eventList]

    response = {
        'type': body['type'],
        'payload': {
            'events': events
        }
    }

    return [response], 200
