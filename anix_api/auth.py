import requests
from .request_handler import AnixRequestsHandler
from .errors import AnixAuthError, AnixInitError

SING_UP = "auth/signUp"
SING_UP_VERIFY = "auth/verify"
SING_IN = "auth/signIn"
FIREBASE = "/auth/firebase"

def check_code(c):
	if c==0:
		return True
	return False

class AnixAuth(AnixRequestsHandler):

	def __init__(self, user):
		super(AnixAuth, self).__init__()
		self.user = user

	def _parse_response(self, data):
		ready = data.json()
		ready.update({"status_code": res.status_code})

		if not check_code(ready['code']):
			print(res.text+"\n\n")
			raise AnixAuthError("auth not ok")

		return ready

	def sing_in(self):
		type(self.user)
		payload = {"login": self.user.login, "password": self.user.password}
		res  = self.post(SING_IN, payload)
		
		ready = res.json()
		ready.update({"status_code": res.status_code})

		if not check_code(ready['code']):
			print(res.text+"\n\n")
			raise Exception("auth not ok")

		self.id = ready["profile"]["id"]
		self.user.id = ready["profile"]["id"]
		self.token = ready["profileToken"]["token"]
		self.user.token = ready["profileToken"]["token"]

		return ready

	def sing_up(self, email):
		raise AnixInitError("AnixAuth.sing_up() - Not ready for use.")
		payload = {"login": self.user.login, "password": self.user.password, "email": email}
		pes1 = self.post(SING_UP, payload).json()

		print(f"Code sended to {email}.")
		code = input("Please input code from mail: ")
		res = self.sing_up_verufy(code, pes1["hash"], True)
		return self._parse_response(res)

	def sing_up_verufy(self, code, _hash, local=False):
		payload = {"login": self.user.login, "password": self.user.password, "email": email, "code": code, "hash": _hash}
		res = self.post(SING_UP_VERIFY, payload)
		if local:
			return res
		return res.json()

	def firebase(self, payload={}):
		return self._parse_response(self.post(FIREBASE, payload))
