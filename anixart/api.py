# -*- coding: utf-8 -*-

from .auth import AnixAuth
from .collections import AnixCollection
from .endpoints import VOICE
from .errors import AnixInitError, AnixAuthError
from .profile import AnixProfile
from .release import AnixRelease
from .request_handler import AnixRequestsHandler


class AnixOther(AnixRequestsHandler):
    def __init__(self, user):
        super(AnixOther, self).__init__(user.token)
        self._get = super().get
        self.get = None
        self.post = None

    def voice(self):
        return self._get(VOICE).json()


class AnixUserAccount:
    def __init__(self, login, password, need_reg=False, email="", config_file="anixart_login.json"):
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

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_token(self):
        return self.token

    def get_id(self):
        return self.id


class AnixAPIRequests:

    def __init__(self, user):
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

        if not isinstance(user, AnixUserAccount):
            raise AnixInitError('Use class "AnixUserAccount" for user.')

        self.auth = AnixAuth(user)

        if user.need_reg:
            self.auth.sing_up()
        else:
            if user.token is None:
                self.auth.sing_in()

        self.me = user
        self.profile = AnixProfile(user)
        self.collection = AnixCollection(user)
        self.coll = self.collection
        self.other = AnixOther(user)
        self.release = AnixRelease(user)


