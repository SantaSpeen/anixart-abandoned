from .auth import AnixAuth
from .request_handler import AnixRequestsHandler
from .errors import AnixInitError, AnixAuthError

class AnixUserAccount:
	def __init__(self, login, password):
		self.login = login
		self.password = password
		if not isinstance(login, str) or not isinstance(password, str):
			raise AnixAuthError("Use normal auth data. In string.")
		self.token = None
		self.id = None

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

		if user.token==None:
			self.auth.sing_in()

		self.user = user

