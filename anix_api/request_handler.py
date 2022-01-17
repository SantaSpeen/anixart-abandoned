import requests

API_URL = "https://api.anixart.tv/"

class AnixRequestsHandler:

	def __init__(self):
		super()
		self.s = requests.Session()
		self.s.headers = {'User-Agent': 'AnixartApp/7.8.1-21090118 (Android 8.1.1; SDK 30; arm64-v8a; Android; ru)'}
	
	def post(self, method, payload={}):
		res = self.s.post(API_URL+method, data=payload)
		return res

	def get(self, method, payload={}):
		res = self.s.get(API_URL+method, params=payload)
		return res
