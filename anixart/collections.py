from .request_handler import AnixRequestsHandler
from .methods import 

class AnixCollectionBase(AnixRequestsHandler):
	def __init__(self, user):
		super(AnixCollectionBase, self).__init__(user.token)
		self.id = user.id
		self._get = super().get
		self._post = super().post

	def _parse_uid(self, uid):
		if uid == None:
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