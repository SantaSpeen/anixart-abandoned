# -*- coding: utf-8 -*-

from .endpoints import COLLECTION, COLLECTION_RELEASES, COLLECTION_LIST, COLLECTION_SEARCH
from .endpoints import COLLECTION_COMMENTS, COLLECTION_COMMENTS_ADD, COLLECTION_COMMENTS_VOTE, COLLECTION_COMMENTS_VOTES
from .endpoints import COLLECTION_COMMENTS_REPLIES, COLLECTION_COMMENTS_EDIT, COLLECTION_COMMENTS_DELETE
from .request_handler import AnixRequestsHandler


class AnixCollectionsBase(AnixRequestsHandler):
    def __init__(self, user):
        super(AnixCollectionsBase, self).__init__(user.token)
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

    def get(self, cid, page=0):
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


class AnixCollections(AnixCollectionsBase):

    def get(self, cid):
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
        return self._post(COLLECTION_SEARCH.format(str(page)), payload).json()


class AnixCollection(AnixCollections):

    def __init__(self, user):
        super().__init__(user)
        self.comments = AnixCollectionsComments(user)
