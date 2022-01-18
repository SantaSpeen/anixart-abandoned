# anixart
#### Non-offical Anixart API wrapper. 
* Description:
	* **EN**: Wrapper for using the anixart API, the best application for watching anime in the CIS countries. From myself I can say that the library was created for informational purposes only. I do not advise you to do such things as cheat likes,have respect for the project. If complaints are received from the project administration, then access to the repository will be limited.
	* **RU**: Враппер для использования anixart API, наилучшего приложения для просмотра аниме на территории стран СНГ.  От себя могу сказать, что библиотека создана лишь для ознакомления. Не советую заниматься такимим вещами как накрутка лайков, имейте уважение к проекту. Если поступят жалобы от администрации проекта, то доступ к репозиторию будет ограничен.


* Endpoints: [here](https://github.com/SantaSpeen/anixart/blob/master/anixart/methods.py)
* Contacts: [Vk](https://vk.com/l.vindeta "Vk"), [Tg](https://t.me/id01234 "Tg").

### Use:
```python3
from anixart import AnixUserAccount, AnixAPI

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
	- Firebase -> `anix.auth.firebase()`
	- Change password -> `anix.auth.change_password(old_pass, new_pass)`

* Profile:
	- get -> `anix.profile.get(uid)`
	- history  -> `anix.profile.history(uid, page)`
	- blocklist  -> `anix.profile.blocklist(page)`
	- friends: 
		* get -> `anix.profile.friends.get(uid, page)`
		* incoming -> `anix.profile.friends.incoming()`
		* outgoing -> `anix.profile.friends.outgoing()`
		* add -> `anix.profile.friends.add(uid)`
		* accept -> `anix.profile.friends.accept(uid)`
		* remove -> `anix.profile.friends.remove(uid)`
	- vote: 
		* voted -> `anix.profile.vote.voted(uid, page)`
		* unvoted -> `anix.profile.vote.unvoted(page)`
	- edit: 
		* status -> `anix.profile.edit.status(text)`
		* social -> `anix.profile.edit.social(instId, tgId, vkId, ttId)`

### In plans:

* Profile:
	- list:
		* get:
			- watching
			- plan
			- watched
			- postponed
			- thrown
			- history
			- favorite 
			- collections
		* add
	- edit:
		* avatar
		* notification:
			- episode
			- comment
			- status
			- voice (type)
			- collection

* Release:
	- get
	- vote:
		* add
		* delite
	- comment:
		* get 
		* vote
		* add
	- random

* Collections:
	- get
	- my:
		* get
		* create
		* edit
		* delite
	- favorite:
		* get
		* add
		* delite
	- comment:	
		* get
		* add
		* edit
		* votes
		* delite

* Discover:
	- interesting
	- watching
	- discussing
	- comments
	- schedule

* Filter
	- get

* Voice:
	- get

* Episode:
	- get:
		- voice
		- player
		- video
	- set:
		- watch
		- unwatch

* Notification:
	- In work.
 