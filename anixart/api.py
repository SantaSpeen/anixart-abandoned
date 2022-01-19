# -*- coding: utf-8 -*-

from .auth import AnixAuth
from .collections import AnixCollection
from .errors import AnixInitError, AnixAuthError
from .methods import VOICE
from .profile import AnixProfile
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
    def __init__(self, login, password, need_reg=False, mail="", config_file="anixart_login.json"):
        """
        Info:

        Anixart login class object.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Usage:

        >>> anix_user = AnixUserAccount("login", "password", need_reg=False, mail="", config_file="anixart_login.json")

        :param login: Anixart nick
        :param password: Anixart password
        :param need_reg: If use use new account, set True
        :param mail: Real email for registration.
        :param config_file: Patch to anixart login data.

        :type login: str
        :type password: str
        :type need_reg: bool
        :type mail: str
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
            if mail is None:
                raise AnixAuthError("Pls input mail.")
        self.mail = mail
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


