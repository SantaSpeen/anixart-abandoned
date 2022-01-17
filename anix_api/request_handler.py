import requests
import random
import json
from .errors import AnixAPIRequestError

API_URL = "https://api.anixart.tv"

class AnixRequestsHandler:

	def __init__(self, token=None):
		self.s = requests.Session()
		self.s.headers = {'User-Agent': 'AnixartApp/7.9-21101018 (Android 11; SDK 30; arm64-v8a; samsung SM-A705FN; ru)'}
		#self.s.headers.update({"Sign": "TlNwOFhxQklPQUFjU2JTZEZKQnNTWm2yQXBCZ3RNY4ZaZlduVDNXN4c3U5VZWlhSWTQxMVpzM3VTZks5azRYb2NKaXhTSk02Njc5fTc6Zzg5MzVoMzhkZzkwZmRnODg7aGVkNGc6NTFkOThnZ5NxLndhbWp6d5NqeC7lcm3iZXZ6aFR7MDF3VFlS8AL4r58u"}
		self.token=token
	
	def post(self, method, payload={}, is_json=False):

		tok = ""
		if payload.get("token")==None:
			if self.token!=None:
				payload.update({"token": self.token}) 
				tok = "?token="+self.token

		if is_json:
			self.s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
			self.s.headers.update({"Content-Length": str(len(str(payload)))})
			res = self.s.post(API_URL+method+tok, json=payload)
		else:
			res = self.s.post(API_URL+method+tok, data=payload)

		if res.json().get("error"):
			raise AnixAPIRequestError(f"\n==========ANIX API ERROR==========\nURL: POST {res.url};\nDATA: {payload}\nHEADERS: {self.s.headers}\nError: {res.json().get('error')}\n")

		self.s.headers["Content-Type"] = None
		self.s.headers["Content-Length"] = None

		return res

	def get(self, method, payload={}):
		if payload.get("token")==None:
			if self.token!=None:
				payload.update({"token": self.token}) 
		res = self.s.get(API_URL+method, params=payload)

		if res.json().get("error"):
			raise AnixAPIRequestError(f"\n==========ANIX API ERROR==========\nURL: GET {res.url};\nDATA: {payload}\nHEADERS: {self.s.headers}\nError: {res.json().get('error')}\n")

		return res
