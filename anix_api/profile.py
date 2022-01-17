from .request_handler import AnixRequestsHandler

# _get
PROFILE = "/profile/{}" # + profile id
PROFILE_NICK_HISTORY = "/profile/login/history/all/{}/{}" # profile id / page

FRIENDS =  "/profile/friend/all/{}/{}"# profile id / page
FRIENDS_RQ_IN = "/profile/friend/requests/in/last"
FRIENDS_RQ_OUT = "/profile/friend/requests/out/last"
FRIENDS_SEND = "/profile/friend/request/send/{}" # profile id
FRIENDS_REMOVE = "/profile/friend/request/remove/{}" # profile id

VOTE_VOTED = "/profile/vote/release/voted/{}/{}" # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}" # page

BLOCKLIST = "/profile/blocklist/all/{}" # page

# POST
EDIT_AVATAR = "/profile/preference/avatar/edit"
EDIT_STATUS = "/profile/preference/status/edit"
EDIT_SOCIAL = "/profile/preference/social/edit"

class AnixProfileBase(AnixRequestsHandler):
	def __init__(self, user):
		super(AnixProfileBase, self).__init__(user.token)
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

	def status(self, text):
		return self._post(EDIT_STATUS, {"status": str(text)}, True).json()

	def social(self, inst="", tg="", vk="", tt=""):
		payload = {"instPage": inst,"tgPage": tg,"ttPage": tt,"vkPage": vk}
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
		token = user.token
		super(AnixProfile, self).__init__(user)
		self.friends = AnixUsersFriends(user)
		self.vote = AnixUsersVote(user)
		self.edit = AnixUsersEdit(user)
		