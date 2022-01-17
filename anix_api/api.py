from .auth import AnixAuth
from .request_handler import AnixRequestsHandler
from .errors import AnixInitError, AnixAuthError
from .profile import AnixProfile

class AnixUserAccount:
	def __init__(self, login, password, need_reg=False, mail=None):
		self.login = login
		self.password = password
		if not isinstance(login, str) or not isinstance(password, str):
			raise AnixAuthError("Use normal auth data. In string.")
		self.token = None
		self.id = None

		self.need_reg = need_reg
		if need_reg:
			if mail==None:
				raise AnixAuthError("Pls input mail.")
		self.mail = mail

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
		if not isinstance(user, AnixUserAccount):
			raise AnixInitError('Use class "AnixUserAccount" for user.')

		self.auth = AnixAuth(user)

		if user.need_reg:
			self.auth.sing_up(user.mail)
		else:
			if user.token==None:
				self.auth.sing_in()

		self.me = user
		self.profile = AnixProfile(user)

