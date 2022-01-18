import requests
import random
import json
from .errors import AnixAPIRequestError
from .methods import API_URL


class AnixRequestsHandler:

	def __init__(self, token=None):
		self.s = requests.Session()
		self.s.headers = {'User-Agent': 'AnixartAPIWrapper/0.2.2-432 (Linux; Android 12; SantaSpeen anixAPI Build/432)'}
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
