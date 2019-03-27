#!/usr/bin/env python3

import os

import pytest
import requests

from app import app


class TestConnexion:
    """The base test providing auth and flask clients to other tests
    """
    cache: dict = {}
    CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')

    #@requests_mock.mock()
    @pytest.fixture(scope='function')
    def client(self, requests_mock):
        requests_mock.post(f'{self.CENTRAL_NODE_BASE_URL}/monitoring', text='', status_code=204)
        with app.app.test_client() as c:
            yield c
            app.registerThread.stop()
