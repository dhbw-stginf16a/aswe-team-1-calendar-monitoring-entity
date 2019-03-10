#!/usr/bin/env python3

import logging

from api.models.UserCalendar import CALENDAR_MANAGER

logger = logging.getLogger(__name__)

def eventToJSON(event):
    return {
        'name': event.name,
        'begin': event.begin.isoformat(),
        'end': event.end.isoformat(),
        'description': event.description,
        'location': event.location,
        'categories': list(event.categories)
    }
