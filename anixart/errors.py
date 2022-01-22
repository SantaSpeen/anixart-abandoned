# -*- coding: utf-8 -*-

"""
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""


class AnixInitError(Exception):
    pass


class AnixAuthError(Exception):
    pass


class AnixAuthEmailAlreadyRegistered(Exception):
    pass


class AnixAuthLoginAlreadyRegistered(Exception):
    pass


class AnixAuthLoginEnterEmail(Exception):
    pass


class AnixAPIRequestError(Exception):
    pass


class AnixAPIError(Exception):
    pass
