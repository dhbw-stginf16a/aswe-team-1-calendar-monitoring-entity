#!/usr/bin/env python3

import logging
import os
import threading
import time

import connexion
from flask_cors import CORS

from api.models.CalendarUpdateManager import CalendarUpdateManager
from api.models.RegistrationThread import RegistrationThread

logger = logging.getLogger(__name__)


CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')
OUR_URL = os.environ.setdefault('OWN_URL', 'http://localhost:5000')

app = connexion.App(__name__, specification_dir='openapi/')
app.add_api('openapi.yml')

# Set CORS headers
CORS(app.app)

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

logger.info('App initialized')

# Start the update manager thread
updater = CalendarUpdateManager()

logger.info('Updater intialized')

app.registerThread = RegistrationThread(CENTRAL_NODE_BASE_URL, OUR_URL)
app.registerThread.start()
