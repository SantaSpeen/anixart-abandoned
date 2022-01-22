# -*- coding: utf-8 -*-

"""
This module implements the API profile requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""
# Edit methods
from .endpoints import EDIT_STATUS, EDIT_SOCIAL, AnixList, LISTS
# Friends methods
from .endpoints import FRIENDS, FRIENDS_RQ_IN, FRIENDS_RQ_OUT, FRIENDS_SEND, FRIENDS_REMOVE
# Profile methods
from .endpoints import PROFILE, PROFILE_NICK_HISTORY
# Blocklist methods
from .endpoints import PROFILE_BLACKLIST, PROFILE_BLACKLIST_ADD, PROFILE_BLACKLIST_REMOVE
# Vote methods
from .endpoints import VOTE_VOTED, VOTE_UNVOTED

from .request_handler import AnixRequestsHandler


class AnixProfileBase(AnixRequestsHandler):
    def __init__(self, user, part: str):
        super(AnixProfileBase, self).__init__(user.token, user._session, "anixart.profile."+part)
        self.id = user.id
        self._get = super().get
        self._post = super().post

    def _parse_uid(self, uid):
        if uid is None:
            uid = self.id
        uid = str(uid)
        return uid

    def _parse_args(self, uid, page):
        uid = self._parse_uid(uid)
        page = str(page)
        return [uid, page]


class AnixUsersFriends(AnixProfileBase):

    def get(self, uid=None, page=0, **kwargs):
        uid, page = self._parse_args(uid, page)
        return self._get(FRIENDS.format(uid, page)).json()

    def incoming(self):
        return self._get(FRIENDS_RQ_IN).json()

    def outgoing(self):
        return self._get(FRIENDS_RQ_OUT).json()

    def add(self, uid):
        uid = self._parse_uid(uid)
        return self._get(FRIENDS_SEND.format(uid)).json()

    def accept(self, uid):
        return self.add(uid)

    def remove(self, uid):
        uid = self._parse_uid(uid)
        return self._get(FRIENDS_REMOVE.format(uid)).json()


class AnixUsersVote(AnixProfileBase):

    def voted(self, uid=None, page=0):
        uid, page = self._parse_args(uid, page)
        return self._get(VOTE_VOTED.format(uid, page)).json()

    def unvoted(self, page=0):
        return self._get(VOTE_UNVOTED.format(str(page))).json()


class AnixUsersEdit(AnixProfileBase):

    def avatar(self, photo):
        print("AnixAPI.profile.edit.avatar() not ready.")
        return {"photo", photo}

        # return self._post(EDIT_AVATAR).json()

    def status(self, text):
        return self._post(EDIT_STATUS, {"status": str(text)}, True).json()

    def social(self, inst="", tg="", vk="", tt=""):
        payload = {"instPage": inst, "tgPage": tg, "ttPage": tt, "vkPage": vk}
        return self._post(EDIT_SOCIAL, payload, True).json()


class AnixUsersBlocklist(AnixProfileBase):

    def get(self, page=0, **kwargs):
        return self._get(PROFILE_BLACKLIST.format(str(page))).json()

    def add(self, uid):
        return self._get(PROFILE_BLACKLIST_ADD.format(str(uid))).json()

    def remove(self, uid):
        return self._get(PROFILE_BLACKLIST_REMOVE.format(str(uid))).json()


class AnixUsersList(AnixProfileBase):

    def get(self, uid=None, list_id: AnixList = AnixList.WATCHING, page=0):
        """
        :type uid: int
        :type list_id: AnixList
        :type page: int
        """
        uid = self._parse_uid(uid)
        return self._get(LISTS.format(uid, list_id, page)).json()


class AnixUsers(AnixProfileBase):

    def get(self, uid=None, **kwargs):
        uid = self._parse_uid(uid)
        return self._get(PROFILE.format(uid)).json()

    def history(self, uid=None, page=0):
        uid, page = self._parse_args(uid, page)
        return self._get(PROFILE_NICK_HISTORY.format(uid, page)).json()


class AnixProfile(AnixUsers):
    def __init__(self, user):
        super(AnixProfile, self).__init__(user, "AnixUsers")
        self.__user = user
        self.__friends = None
        self.__vote = None
        self.__edit = None
        self.__blocklist = None
        self.__list = None

    @property
    def friends(self):
        if self.__friends is None:
            self.__friends = AnixUsersFriends(self.__user, "AnixUsersFriends")
        return self.__friends

    @property
    def vote(self):
        if self.__vote is None:
            self.__vote = AnixUsersVote(self.__user, "AnixUsersVote")
        return self.__vote

    @property
    def edit(self):
        if self.__edit is None:
            self.__edit = AnixUsersEdit(self.__user, "AnixUsersEdit")
        return self.__edit

    @property
    def blocklist(self):
        if self.__blocklist is None:
            self.__blocklist = AnixUsersBlocklist(self.__user, "AnixUsersBlocklist")
        return self.__blocklist

    @property
    def bl(self):
        if self.__blocklist is None:
            self.__blocklist = AnixUsersBlocklist(self.__user, "AnixUsersBlocklist")
        return self.__blocklist

    @property
    def list(self):
        if self.__list is None:
            self.__list = AnixUsersList(self.__user, "AnixUsersList")
        return self.__list
