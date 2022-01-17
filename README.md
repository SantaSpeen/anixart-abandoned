# anix_api - Anixart API project. (non-offical)

### Use:
```python3
from anix_api import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

print(f"Token: {anix.me.get_token()}; ID: {anix.me.get_id()}")

profile = anix.profile.get()['profile']
nick = profile['login']
status = profile['status']
vk = profile['vk_page']
tg = profile['tg_page']
inst = profile['inst_page']
tt = profile['tt_page']
reg_date = profile['register_date']

print(f"Nick: {nick}\nStatus: {status}\nVk: {vk}\nTg: {tg}\nInst: {inst}\nTt: {tt}\nRegister date: {reg_date}")
```

### Ready now:

uid - User Id, default: self.
page - Page if data, default: 0.

* Me (class with login data): 
	- login -> anix.me.get_login()
	- password -> anix.me.get_password()
	- token -> anix.me.get_token()
	- id -> anix.me.get_id()

* Auth:
	- Sing In -> Do not use this metod. Lib auto singing in.
	- Sing Up -> Do not use this metod. Lib auto singing up. Need real email!
	- Firebase -> anix.auth.firebase()

* Profile:
	- get -> anix.profile.get(uid)
	- history  -> anix.profile.history(uid, page)
	- history  -> anix.profile.blocklist(page)
	- friends: 
		* get -> anix.profile.friends.get(uid, page)
		* incoming -> anix.profile.friends.incoming()
		* outgoing -> anix.profile.friends.outgoing()
		* add -> anix.profile.friends.add(uid)
		* accept -> anix.profile.friends.accept(uid)
		* remove -> anix.profile.friends.remove(uid)
	- vote: 
		* voted -> anix.profile.vote.voted(uid, page)
		* unvoted -> anix.profile.vote.unvoted(page)
	- edit: 
		* status -> anix.profile.edit.status(text)
		* social -> anix.profile.edit.social(instId, tgId, vkId, ttId)
		* avatar -> fixing.