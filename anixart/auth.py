# -*- coding: utf-8 -*-

"""
This module implements the API auth requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

from .endpoints import CHANGE_PASSWORD
from .errors import AnixAuthError
from .request_handler import AnixRequestsHandler


def _parse_response(data):
    ready = data.json()
    ready.update({"status_code": data.status_code})

    code = ready['code']
    if code != 0:
        if code == 2:
            raise AnixAuthError("Incorrect login.")
        if code == 3:
            raise AnixAuthError("Incorrect password.")
        print(data.text + "\n\n")
        raise AnixAuthError("Unknown auth error.")

    return ready


class AnixAuth(AnixRequestsHandler):

    def __init__(self, user):
        super(AnixAuth, self).__init__(None, user.session, "anixart.auth.AnixAuth")
        self.user = user
        self.filename = user.config_file

    def _save_config(self, data):
        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def _open_config(self):
        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def sing_in(self, token: str = None, id: int = None):

        if token and id:
            self.user.id = id
            self.user.token = token

        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def sing_up(self):
        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def sing_up_verify(self, code, _hash, email, local=False):
        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def firebase(self, payload=None):
        raise AnixAuthError("Метод убран по просьбе администратора проекта.")

    def change_password(self, old, new):
        return self.get(CHANGE_PASSWORD, {"current": old, "new": new, "token": self.user.token})
