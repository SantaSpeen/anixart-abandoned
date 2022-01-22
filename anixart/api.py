# -*- coding: utf-8 -*-

"""
General Anixart API class.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

import logging

import requests

from .auth import AnixAuth
from .collections import AnixCollection
from .endpoints import TYPE, HISTORY, TOGGLES
from .errors import AnixInitError, AnixAuthError
from .profile import AnixProfile
from .release import AnixRelease
from .request_handler import AnixRequestsHandler

_lc = 6
_log_name = "file:%-29s -> %s" % ("<anixart.api:%-4i>", "%s")


class AnixUserAccount:
    def __init__(self, login, password, need_reg=False, email="", config_file="anixart_login.json", **kwargs):
        """
        Info:

        Anixart login class object.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Usage:

        >>> anix_user = AnixUserAccount("login", "password", need_reg=False, mail="", config_file="anixart_login.json")
        >>> print(anix_user.login)

        Availible params:
        ~~~~~~~~~~~~~~~~~

        * login -> Your anixart nick
        * password -> Your anixart password
        * need_reg -> If you need new account, set True.
        * mail -> Real email for registration.
        * config_file -> Patch to anixart login cache.

        :param login: Your anixart nick
        :param password: Anixart password
        :param need_reg: If you need new account, set True.
        :param email: Real email for registration.
        :param config_file: Patch to anixart login cache.

        :type login: str
        :type password: str
        :type need_reg: bool
        :type email: str
        :type config_file: str

        :return: :class:`AnixUserAccount <anixart.api.AnixUserAccount>` object
        """
        self.__kwargs = kwargs
        log_level = logging.CRITICAL
        log_format = '[%(name)-43s] %(levelname)-5s: %(message)s'
        if kwargs.get("loglevel") is not None:
            log_level = kwargs.get("loglevel")
        if kwargs.get("logformat") is not None:
            log_format = kwargs.get("logformat")
        logging.basicConfig(level=log_level, format=log_format)
        self.__log = logging.getLogger("anixart.api.AnixUserAccount")

        self.__log.debug(_log_name, 70, "__init__ - INIT")

        self.login = login
        self.password = password
        if not isinstance(login, str) or not isinstance(password, str):
            raise AnixAuthError("Use normal auth data. In string.")
        self.token = None
        self.id = None

        self.need_reg = need_reg
        if need_reg:
            if email is None:
                raise AnixAuthError("Pls input mail.")
        self.mail = email
        self.config_file = config_file

        self._session = requests.Session()
        self.__log.debug(_log_name, 87, f"{str(self)}")
        self.__log.debug(_log_name, 88, "__init__() - OK")

    def __str__(self):
        return f'AnixUserAccount(login="{self.login}", password="{self.password}", need_reg="{self.need_reg}", ' \
               f'email="{self.mail}", config_file="{self.config_file}", kwargs="{self.__kwargs}")'

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_token(self):
        return self.token

    def get_id(self):
        return self.id


class AnixOther(AnixRequestsHandler):
    def __init__(self, user: AnixUserAccount):
        super(AnixOther, self).__init__(user.token, user._session)
        self.__get = super().get

    def type(self):
        return self.__get(TYPE).json()

    def history(self, page=0):
        return self.__get(HISTORY.format(str(page))).json()

    def toggles(self, ver: int, is_beta: bool):
        return self.__get(TOGGLES.format(str(ver), is_beta)).json()


class AnixAPI:

    def __init__(self, user: AnixUserAccount):
        """
        Info:

        Anixart API class object.
        ~~~~~~~~~~~~~~~~~~~~~~~~~

        Usage:

        >>> anix_user = AnixUserAccount("login", "password", need_reg=False, mail="", config_file="anixart_login.json")
        >>> anix = AnixAPI(anix_user)

        Availible classes:
        ~~~~~~~~~~~~~~~~~

        * auth
        * profile
        * collection
        * coll
        * other

        :param user: :class:`AnixUserAccount <anixart.api.AnixUserAccount>` object
        :return: :class:`AnixAPIRequests <anixart.api.AnixAPIRequests>` object
        """

        self.__log = logging.getLogger("anixart.api.AnixAPI")

        self.__log.debug(_log_name, 145+_lc, "__init__ - INIT")

        if not isinstance(user, AnixUserAccount):
            self.__log.critical('Use anixart.api.AnixUserAccount for user.')
            raise AnixInitError('Use class "AnixUserAccount" for user.')

        self.auth = AnixAuth(user)

        if user.need_reg:
            self.__log.debug(_log_name, 154+_lc, "User set need_reg=True..")
            self.auth.sing_up()
        else:
            if user.token is None or user.id is None:
                self.__log.debug(_log_name, 158+_lc, "Singing in..")
                self.auth.sing_in()

        self.me = user
        self.__profile = None
        self.__collection = None
        self.__other = None
        self.__release = None

        self.__log.debug(_log_name, 167+_lc, "__init__ - OK.")

    def __str__(self):
        return f'AnixAPI({self.me})'

    @property
    def profile(self):
        self.__log.debug(_log_name, 174+_lc, "property func: profile()")
        if self.__profile is None:
            self.__log.debug(_log_name, 176+_lc, "The '__profile' variable has not yet been declared. Initialization.")
            self.__profile = AnixProfile(self.me)
        return self.__profile

    @property
    def collection(self):
        self.__log.debug(_log_name, 182+_lc, "property func: collection()")
        if self.__collection is None:
            self.__log.debug(_log_name, 184+_lc, "The '__collection' variable has not yet been declared. Initialization.")
            self.__collection = AnixCollection(self.me)
        return self.__collection

    @property
    def coll(self):
        self.__log.debug(_log_name, 190+_lc, "property func: coll()")
        if self.__collection is None:
            self.__log.debug(_log_name, 192+_lc, "The '__collection' variable has not yet been declared. Initialization.")
            self.__collection = AnixCollection(self.me)
        return self.__collection

    @property
    def other(self):
        self.__log.debug(_log_name, 198+_lc, "property func: other()")
        if self.__other is None:
            self.__log.debug(_log_name, 200+_lc, "The '__other' variable has not yet been declared. Initialization.")
            self.__other = AnixOther(self.me)
        return self.__other

    @property
    def release(self):
        self.__log.debug(_log_name, 206+_lc, "property func: release()")
        if self.__release is None:
            self.__log.debug(_log_name, 208+_lc, "The '__release' variable has not yet been declared. Initialization.")
            self.__release = AnixRelease(self.me)
        return self.__release
