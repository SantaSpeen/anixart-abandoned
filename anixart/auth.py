# -*- coding: utf-8 -*-

import json

from .errors import AnixAuthError
from .methods import SING_UP, SING_UP_VERIFY, SING_IN, FIREBASE, CHANGE_PASSWORD, PROFILE
from .request_handler import AnixRequestsHandler


def check_code(c):
    if c == 0:
        return True
    return False


class AnixAuth(AnixRequestsHandler):

    def __init__(self, user):
        super(AnixAuth, self).__init__()
        self.user = user
        self.filename = user.config_file

    def _parse_response(self, data):
        ready = data.json()
        ready.update({"status_code": data.status_code})

        if not check_code(ready['code']):
            print(data.text + "\n\n")
            raise AnixAuthError("auth not ok")

        return ready

    def _save_config(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f)
        return data

    def _open_config(self):
        try:
            with open(self.filename, "r") as read_file:
                data = json.load(read_file)
            return data
        except Exception:
            return False

    def sing_in(self):

        config = self._open_config()

        if config:

            uid = config.get("id")
            token = config.get("token")
            if not self.get(PROFILE.format(uid),
                            payload={"token": token}).json().get("is_my_profile") or \
                    self.user.login != config.get("login"):
                print("[ANIXART API] Invalid config file. Re login.")

                self.user.id = uid
                self.user.token = token

            else:
                return config

        payload = {"login": self.user.login, "password": self.user.password}
        res = self.post(SING_IN, payload)

        ready = self._parse_response(res)

        uid = ready["profile"]["id"]
        token = ready["profileToken"]["token"]

        self.user.id = uid
        self.user.token = token

        self._save_config({"id": uid, "token": token, "login": self.user.login})

        return ready

    def sing_up(self):
        email = self.user.mail
        payload = {"login": self.user.login, "password": self.user.password, "email": email}
        res1 = self.post(SING_UP, payload).json()

        print(f"Code sent to {email}.")
        code = input("Please input code from mail: ")
        res2 = self.sing_up_verify(code, res1["hash"], email, True)
        ready = self._parse_response(res2)

        uid = ready["profile"]["id"]
        token = ready["profileToken"]["token"]

        self.user.id = uid
        self.user.token = token

        self._save_config({"id": uid, "token": token, "login": self.user.login})

        return ready

    def sing_up_verify(self, code, _hash, email, local=False):
        payload = {"login": self.user.login, "password": self.user.password, "email": email, "code": code,
                   "hash": _hash}
        res = self.post(SING_UP_VERIFY, payload)
        res_json = res.json()
        if res_json['code'] != 0:
            print("Code not right.")
            code = input("Pls input code again: ")
            return self.sing_up_verify(code, _hash, email, True)
        if local:
            return res
        return

    def firebase(self, payload=None):
        if payload is None:
            payload = {}
        return self._parse_response(self.post(FIREBASE, payload))

    def change_password(self, old, new, token):
        return self.get(CHANGE_PASSWORD, {"current": old, "new": new, "token": token})
