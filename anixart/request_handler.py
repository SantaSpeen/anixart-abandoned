# -*- coding: utf-8 -*-

"""
This module implements the API requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

import requests
from .errors import AnixAPIRequestError
from .methods import API_URL
from .__version__ import __version__, __build__


class AnixRequestsHandler:

    def __init__(self, token=None):
        self.s = requests.Session()
        self.s.headers = {'User-Agent': f'AnixartAPIWrapper/{__version__}-{__build__} (Linux; Android 12; SantaSpeen anixAPI Build/{__build__})'}
        self.token = token

    def post(self, method, payload=None, is_json=False, **kwargs):
        if payload is None:
            payload = {}

        tok = ""
        if payload.get("token") is None:
            if self.token is not None:
                payload.update({"token": self.token})
                tok = "?token=" + self.token

        if is_json:
            self.s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
            self.s.headers.update({"Content-Length": str(len(str(payload)))})
            res = self.s.post(API_URL + method + tok, json=payload, **kwargs)
        else:
            res = self.s.post(API_URL + method + tok, data=payload, **kwargs)

        if res.json().get("error"):
            raise AnixAPIRequestError(f"\n\nURL: POST {res.url};\nDATA: {payload}\nError: {res.json().get('error')}\n")

        self.s.headers["Content-Type"] = None
        self.s.headers["Content-Length"] = None

        return res

    def get(self, method, payload=None, **kwargs):
        if payload is None:
            payload = {}

        if payload.get("token") is None:
            if self.token is not None:
                payload.update({"token": self.token})

        res = self.s.get(API_URL + method, params=payload, **kwargs)

        if res.json().get("error"):
            raise AnixAPIRequestError(f"\n\nURL: GET {res.url};\nDATA: {payload}\nError: {res.json().get('error')}\n")

        return res
