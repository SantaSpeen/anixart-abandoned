# -*- coding: utf-8 -*-

from .request_handler import AnixRequestsHandler
from .methods import COLLECTION, COLLECTION_RELEASES, COLLECTION_LIST

from .methods import COLLECTION_COMMENTS, COLLECTION_COMMENTS_ADD, COLLECTION_COMMENTS_VOTE, COLLECTION_COMMENTS_VOTES
from .methods import COLLECTION_COMMENTS_REPLIES, COLLECTION_COMMENTS_EDIT, COLLECTION_COMMENTS_DELETE


class AnixCollectionBase(AnixRequestsHandler):
	def __init__(self, user):
		super(AnixCollectionBase, self).__init__(user.token)
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


class AnixCollection(AnixCollectionBase):

	def get(self):
		pass