# -*- coding: utf-8 -*-

"""
This module implements the API requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

import requests

from .__version__ import __version__, __build__
from .endpoints import API_URL
from .errors import AnixAPIRequestError, AnixAPIError, AnixAuthError, AnixAuthLoginAlreadyRegistered, \
    AnixAuthLoginEnterEmail


def parse_res_code(res, payload, m, h):
    json = res.json()

    error = json.get("error")
    code = json.get("code")

    if error:
        # raise AnixAPIRequestError(f"\n\nURL: POST {res.url};\nDATA: {payload}\nError: {res.json().get('error')}\n")
        raise AnixAPIRequestError(f"Internal server error: {error}; Payload: {payload}")

    if code == 0:
        return
    elif code == 2:
        raise AnixAPIError(f"Incorrect input data.; Json: {json}")
    elif code == 3:
        if json.get("hash") is not None:
            raise AnixAuthLoginEnterEmail(f"Pls input mail; Json: {json}")
        raise AnixAuthError(f"Incorrect password; Json: {json}")
    elif code == 5:
        raise AnixAuthLoginAlreadyRegistered(f"Login already registered; Json: {json}")
    elif code == 7:
        # Reg code not right.
        # print("code 7")
        return
        # raise AnixAuthEmailAlreadyRegistered(f"E-mail already registered; Json: {json}")
    elif code == 8:
        # print("code 8")
        return
    elif code >= 400:
        raise AnixAPIRequestError(f"\n\n"
                                  f"Send this info to author.\n"
                                  f"URL: {m} {res.url}\n"
                                  f"Status code: {res.status_code}\n"
                                  f"Res headers: {res.headers}\n"
                                  f"Req headers: {h}\n"
                                  f"Server res: {json}\n"
                                  f"Client req: {payload}\n")
    else:
        raise AnixAPIError(f"Server send error code: {code}; Json: {json}")


class AnixRequestsHandler:

    def __init__(self, token=None):
        self.s = requests.Session()
        self.s.headers = {
            'User-Agent': f'AnixartAPIWrapper/{__version__}-{__build__} (Linux; Android 12; SantaSpeen anixAPI Build/{__build__})'}
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

        parse_res_code(res, payload, "POST", self.s.headers)

        self.s.headers["Content-Type"] = ""
        self.s.headers["Content-Length"] = ""

        return res

    def get(self, method, payload=None, **kwargs):
        if payload is None:
            payload = {}

        if payload.get("token") is None:
            if self.token is not None:
                payload.update({"token": self.token})

        res = self.s.get(API_URL + method, params=payload, **kwargs)

        parse_res_code(res, payload, "GET", self.s.headers)

        return res
