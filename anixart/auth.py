import requests
import json
from .request_handler import AnixRequestsHandler
from .errors import AnixAuthError, AnixInitError
from .methods import SING_UP, SING_UP_VERIFY, SING_IN, FIREBASE, CHANGE_PASSWORD, PROFILE


def check_code(c):
	if c==0:
		return True
	return False

class AnixAuth(AnixRequestsHandler):

	def __init__(self, user):
		super(AnixAuth, self).__init__()
		self.user = user
		self.filename = user.config_file

	def _parse_response(self, data):
		ready = data.json()
		ready.update({"status_code": data.status_code})

		if not check_code(ready['code']):
			print(res.text+"\n\n")
			raise AnixAuthError("auth not ok")

		return ready

	def _save_config(self, data):
		with open(self.filename, "w") as f:
			json.dump(data, f)
		return data

	def _open_config(self):
		try:
			with open(self.filename, "r") as read_file:
				data = json.load(read_file)
			return data
		except Exception as e:
			return False
		

	def sing_in(self):

		config = self._open_config()

		if config:
			self.user.id = config.get("id")
			self.user.token = config.get("token")
			if not self.get(PROFILE.format(self.user.id), payload={"token":self.user.token}).json().get("is_my_profile"):
				print("[ANIXART API] Invalid config file. Relogin.")
			else:
				return config

		payload = {"login": self.user.login, "password": self.user.password}
		res  = self.post(SING_IN, payload)
		
		ready = self._parse_response(res)

		uid = ready["profile"]["id"]
		token = ready["profileToken"]["token"]

		self.user.id = uid
		self.user.token = token

		self._save_config({"id": uid, "token": token})

		return ready

	def sing_up(self):
		email = self.user.mail
		payload = {"login": self.user.login, "password": self.user.password, "email": email}
		res1 = self.post(SING_UP, payload).json()

		print(f"Code sended to {email}.")
		code = input("Please input code from mail: ")
		res2 = self.sing_up_verufy(code, res1["hash"], email, True)
		ready = self._parse_response(res2)

		uid = ready["profile"]["id"]
		token = ready["profileToken"]["token"]

		self.user.id = uid
		self.user.token = token

		self._save_config({"id": uid, "token": token})

		return ready

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

