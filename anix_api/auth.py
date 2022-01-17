import requests
from .request_handler import AnixRequestsHandler
from .errors import AnixAuthError, AnixInitError

# POST
SING_UP = "/auth/signUp"
SING_UP_VERIFY = "/auth/verify"
SING_IN = "/auth/signIn"
FIREBASE = "/auth/firebase"

# GET
CHANGE_PASSWORD = "/profile/preference/password/change"

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
		ready.update({"status_code": data.status_code})

		if not check_code(ready['code']):
			print(res.text+"\n\n")
			raise AnixAuthError("auth not ok")

		return ready

	def sing_in(self):
		payload = {"login": self.user.login, "password": self.user.password}
		res  = self.post(SING_IN, payload)
		
		ready = self._parse_response(res)

		self.user.id = ready["profile"]["id"]
		self.user.token = ready["profileToken"]["token"]

		return ready

	def sing_up(self):
		email = self.user.mail
		payload = {"login": self.user.login, "password": self.user.password, "email": email}
		res1 = self.post(SING_UP, payload).json()

		print(f"Code sended to {email}.")
		code = input("Please input code from mail: ")
		res2 = self.sing_up_verufy(code, res1["hash"], email, True)
		ready = self._parse_response(res2)

		self.user.id = ready["profile"]["id"]
		self.user.token = ready["profileToken"]["token"]

	def sing_up_verufy(self, code, _hash, email, local=False):
		payload = {"login": self.user.login, "password": self.user.password, "email": email, "code": code, "hash": _hash}
		res = self.post(SING_UP_VERIFY, payload)
		res_json = res.json()
		if res_json['code'] != 0:
			print("Code not right.")
			code = input("Pls input code again: ")
			return self.sing_up_verufy(code, _hash, email, True)
		if local:
			return res
		return 

	def firebase(self, payload={}):
		return self._parse_response(self.post(FIREBASE, payload))

	def change_password(self, old, new, token):
		return self.get(CHANGE_PASSWORD, {"current": old, "new": new, "token": token})

