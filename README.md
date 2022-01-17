# anix_api - Anixart API project. (non-offical)

### Use:
```python3
from anix_api import AnixUserAccount, AnixAPI

anix_anix_user = AnixUserAccount(login="", password="", need_reg=False, mail="your@mail.tv")
anix = AnixAPI(anix_anix_user)

print(f"Token: {anix.me.get_token()}; ID: {anix.me.get_id()}")

```

### Ready now:

uid - User Id

* Auth:
	- Sing In -> Do not use this metod. Programm auto singing in.
	- Sing Up -> Do not use this metod. Programm auto singing up.
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
		* avatar -> Nothink work.
		* status -> Nothink work.
		* social -> Nothink work.