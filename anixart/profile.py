# -*- coding: utf-8 -*-

# Edit methods
from .methods import EDIT_STATUS, EDIT_SOCIAL, EDIT_AVATAR
# Friends methods
from .methods import FRIENDS, FRIENDS_RQ_IN, FRIENDS_RQ_OUT, FRIENDS_SEND, FRIENDS_REMOVE
# Profile methods
from .methods import PROFILE, PROFILE_NICK_HISTORY
from .methods import VOICE
# Vote methods
from .methods import VOTE_VOTED, VOTE_UNVOTED
from .request_handler import AnixRequestsHandler


class AnixProfileBase(AnixRequestsHandler):
    def __init__(self, user):
        super(AnixProfileBase, self).__init__(user.token)
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

    def get(self, uid=None, page=0):
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
        return {}

        return self._post(EDIT_AVATAR).json()

    def status(self, text):
        return self._post(EDIT_STATUS, {"status": str(text)}, True).json()

    def social(self, inst="", tg="", vk="", tt=""):
        payload = {"instPage": inst, "tgPage": tg, "ttPage": tt, "vkPage": vk}
        return self._post(EDIT_SOCIAL, payload, True).json()


class AnixUsers(AnixProfileBase):

    def get(self, uid=None):
        uid = self._parse_uid(uid)
        return self._get(PROFILE.format(uid)).json()

    def history(self, uid=None, page=0):
        uid, page = self._parse_args(uid, page)
        return self._get(PROFILE_NICK_HISTORY.format(uid, page)).json()

    def blocklist(self, page=0):
        return self._get(PROFILE_NICK_HISTORY.format(str(page))).json()


class AnixProfile(AnixUsers):
    def __init__(self, user):
        super(AnixProfile, self).__init__(user)
        self.friends = AnixUsersFriends(user)
        self.vote = AnixUsersVote(user)
        self.edit = AnixUsersEdit(user)

    def _voice(self):
        return self._get(VOICE).json()
