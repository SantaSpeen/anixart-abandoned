# -*- coding: utf-8 -*-

"""
This module implements the API requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

import logging

import requests

from .__version__ import __version__, __build__
from .endpoints import API_URL
from .errors import AnixAPIRequestError, AnixAPIError, AnixAuthError, AnixAuthLoginAlreadyRegistered, \
    AnixAuthLoginEnterEmail

_log_name = "file:%-28s -> %s" % ("<anixart.request_handler:%-3i>", "%s")


def _parse_res_code(res, payload, m, h):
    json = res.json()

    error = json.get("error")
    code = json.get("code")

    if res.status_code >= 400:
        raise AnixAPIRequestError(f"\n\nANIX API WRAPPER ERROR\n"
                                  f"Send this info to author: https://vk.com/l.vindeta\n"
                                  f"URL: {m} {res.url}\n"
                                  f"Status code: {res.status_code}\n"
                                  f"Res headers: {res.headers}\n"
                                  f"Req headers: {h}\n"
                                  f"Server res: {json}\n"
                                  f"Client req: {payload}\n")

    if error:
        # raise AnixAPIRequestError(f"\n\nURL: POST {res.url};\nDATA: {payload}\nError: {res.json().get('error')}\n")
        raise AnixAPIRequestError(f"Internal server error: {error}; Payload: {payload}")

    if code:
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

    def __init__(self, token: str = None, session: requests.Session = None, _log_class="anixart.request_handler.AnixRequestsHandler"):
        self.__log = logging.getLogger(_log_class)
        self.__log.debug(_log_name, 76, f"__init__ - INIT from {self}")
        if session:
            self.__session = session
        else:
            self.__log.debug(_log_name, 81, "Create new session.")
            self.__session = requests.Session()
        self.__session.headers = {
            'User-Agent': f'AnixartAPIWrapper/{__version__}-{__build__} (Linux; Android 12; SantaSpeen anixAPI Build/{__build__})'}
        self.__token = token

    def post(self, method: str, payload: dict = None, is_json: bool = False, **kwargs):
        if payload is None:
            payload = {}

        url = API_URL + method

        if payload.get("token") is None:
            if self.__token is not None:
                payload.update({"token": self.__token})
                url += "?token=" + self.__token
        else:
            token = kwargs.get("token")
            if token is not None:
                payload.update({"token": token})
                url += "?token=" + token

        kwargs = {"url": url}
        if is_json:
            self.__session.headers.update({"Content-Type": "application/json; charset=UTF-8"})
            self.__session.headers.update({"Content-Length": str(len(str(payload)))})
            kwargs.update({"json": payload})
        else:
            kwargs.update({"data": payload})

        self.__log.debug(_log_name, 108, f"{'json' if is_json else ''} POST {method}; {payload}")
        res = self.__session.post(**kwargs)

        _parse_res_code(res, payload, "POST", self.__session.headers)

        self.__session.headers["Content-Type"] = ""
        self.__session.headers["Content-Length"] = ""

        return res

    def get(self, method: str, payload: dict = None, **kwargs):
        if payload is None:
            payload = {}

        if payload.get("token") is None:
            if self.__token is not None:
                payload.update({"token": self.__token})
        else:
            token = kwargs.get("token")
            if token is not None:
                payload.update({"token": token})

        self.__log.debug(_log_name, 130, f"GET {method}; {payload}")
        res = self.__session.get(API_URL + method, params=payload)

        _parse_res_code(res, payload, "GET", self.__session.headers)

        return res
