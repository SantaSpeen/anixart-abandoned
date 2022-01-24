# -*- coding: utf-8 -*-

"""
This module implements the API collection requests.
:copyright: (c) 2022 by Maxim Khomutov.
:license: MIT
"""

from .endpoints import COLLECTION, COLLECTION_RELEASES, COLLECTION_LIST, SEARCH_COLLECTION
from .endpoints import COLLECTION_COMMENTS, COLLECTION_COMMENTS_ADD, COLLECTION_COMMENTS_VOTE, COLLECTION_COMMENTS_VOTES
from .endpoints import COLLECTION_COMMENTS_REPLIES, COLLECTION_COMMENTS_EDIT, COLLECTION_COMMENTS_DELETE
from .endpoints import COLLECTION_FAVORITE, COLLECTION_FAVORITE_ADD, COLLECTION_FAVORITE_DELETE
from .request_handler import AnixRequestsHandler


class AnixCollectionsBase(AnixRequestsHandler):
    def __init__(self, user):
        super(AnixCollectionsBase, self).__init__(user.token, user.session)
        self._get = super().get
        self._post = super().post

    def _parse_cid(self, cid):
        cid = str(cid)
        return cid

    def _parse_args(self, cid, page):
        cid = self._parse_cid(cid)
        page = str(page)
        return [cid, page]


class AnixCollectionsComments(AnixCollectionsBase):

    def get(self, cid, page=0, **kwargs):
        cid, page = self._parse_args(cid, page)
        return self._get(COLLECTION_COMMENTS.format(cid, page)).json()

    def add(self, cid, message, parent_comment_id=None, reply_to_profile_id=None, spoiler=False):
        payload = {"message": message,
                   "parentCommentId": parent_comment_id,
                   "replyToProfileId": reply_to_profile_id,
                   "spoiler": spoiler}
        cid = str(cid)
        return self._post(COLLECTION_COMMENTS_ADD.format(cid), payload, True).json()

    def vote(self, ccmid, mark):
        ccmid = str(ccmid)
        mark = str(mark)
        return self._get(COLLECTION_COMMENTS_VOTE.format(ccmid, mark)).json()

    def votes(self, ccmid, page=0):
        ccmid = str(ccmid)
        page = str(page)
        return self._get(COLLECTION_COMMENTS_VOTES.format(ccmid, page)).json()

    def replies(self, ccmid, page=0):
        ccmid, page = self._parse_args(ccmid, page)
        return self._post(COLLECTION_COMMENTS_REPLIES.format(ccmid, page), is_json=True).json()

    def edit(self, ccmid, message, spoiler=False):
        payload = {"message": message,
                   "spoiler": spoiler}
        ccmid = str(ccmid)
        return self._post(COLLECTION_COMMENTS_EDIT.format(ccmid), payload, True).json()

    def delete(self, ccmid):
        ccmid = str(ccmid)
        return self._get(COLLECTION_COMMENTS_DELETE.format(ccmid)).json()


class AnixCollectionsFavorite(AnixCollectionsBase):

    def get(self, page=0, **kwargs):
        return self._get(COLLECTION_FAVORITE.format(str(page))).json()

    def add(self, cid):
        cid = self._parse_cid(cid)
        return self._get(COLLECTION_FAVORITE_ADD.format(cid)).json()

    def delete(self, cid):
        cid = self._parse_cid(cid)
        return self._get(COLLECTION_FAVORITE_DELETE.format(cid)).json()


class AnixCollections(AnixCollectionsBase):

    def get(self, cid, **kwargs):
        cid = self._parse_cid(cid)
        return self._get(COLLECTION.format(cid)).json()

    def list(self, page=0):
        page = str(page)
        return self._get(COLLECTION_LIST.format(page)).json()

    def releases(self, cid, page=0):
        cid, page = self._parse_args(cid, page)
        return self._get(COLLECTION_RELEASES.format(cid, page)).json()

    def search(self, query, page=0):
        payload = {"query": query, "searchBy": 0}
        return self._post(SEARCH_COLLECTION.format(str(page)), payload).json()


class AnixCollection(AnixCollections):

    def __init__(self, user):
        super().__init__(user)
        self.__user = user
        self.__comments = None
        self.__favorite = None

    @property
    def comments(self):
        if self.__comments is None:
            self.__comments = AnixCollectionsComments(self.__user)
        return self.__comments

    @property
    def favorite(self):
        if self.__favorite is None:
            self.__favorite = AnixCollectionsFavorite(self.__user)
        return self.__favorite
