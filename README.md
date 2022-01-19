# anixart
#### Non-official Anixart API wrapper. 

**Документация на русском:** [ТЫК](https://anixart.readthedocs.io/ "тык")

* Description:
    * **EN**: Wrapper for using the anixart API, the best application for watching anime in the CIS countries. From myself I can say that the library was created for informational purposes only. I do not advise you to do such things as cheat likes,have respect for the project. If complaints are received from the project administration, then access to the repository will be limited.
    * **RU**: Враппер для использования anixart API, наилучшего приложения для просмотра аниме на территории стран СНГ.  От себя могу сказать, что библиотека создана лишь для ознакомления. Не советую заниматься такимим вещами как накрутка лайков, имейте уважение к проекту. Если поступят жалобы от администрации проекта, то доступ к репозиторию будет ограничен.


* Endpoints: [here](https://github.com/SantaSpeen/anixart/blob/master/anixart/methods.py)
* Contacts: [Vk](https://vk.com/l.vindeta "Vk"), [Tg](https://t.me/id01234 "Tg").

### Install: 
`pip3 install anixart`

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
1. uid - int; User Id, default: self.
2. page - int; Page of data, default: 0.
3. cid - int; Collection id.
4. ccmid - int; Collection comment id.
5. query - str; query text.
6. message - str; Comment text.
7. spoiler - bool; Comment spoiler, default: False.
8. mark - int; Comment vote. Use `AnixComment.UP` or `AnixComment.DOWN`


* Me (class with login data): 
    - login -> `anix.me.get_login()`
    - password -> `anix.me.get_password()`
    - token -> `anix.me.get_token()`
    - id -> `anix.me.get_id()`

* Auth `anix.auth`:
    - Sing In -> Do not use this method. Lib auto singing in.
    - Sing Up -> Do not use this method. Lib auto singing up. Need real email!
    - Firebase -> `anix.auth.firebase()`
    - Change password -> `anix.auth.change_password(old_pass, new_pass)`; Change password.

* Profile `anix.profile`:
    - get -> `anix.profile.get(uid)`; Get profile.
    - history  -> `anix.profile.history(uid, page)`; Get nickname history.
    - blocklist  -> `anix.profile.blocklist(page)`; Get blocked profiles.
    - friends `anix.profile.friends`: 
        * get -> `anix.profile.friends.get(uid, page)`; Get friends.
        * incoming -> `anix.profile.friends.incoming()`; Get incoming friend referrals.
        * outgoing -> `anix.profile.friends.outgoing()`; Get outgoing friend referrals.
        * add -> `anix.profile.friends.add(uid)`; Add friend.
        * accept -> `anix.profile.friends.accept(uid)`; Accept friend.
        * remove -> `anix.profile.friends.remove(uid)`; Remove friend.
    - vote `anix.profile.vote`: 
        * voted -> `anix.profile.vote.voted(uid, page)`; Anime that was voted.
        * unvoted -> `anix.profile.vote.unvoted(page)`; Anime not upvoted.
    - edit `anix.profile.edit`: 
        * status -> `anix.profile.edit.status(text)`; Edit status.
        * social -> `anix.profile.edit.social(instId, tgId, vkId, ttId)`; Edit social (contacts).

* Collections `anix.coll` or `anix.collection`:
    - get -> `anix.coll.get(cid)`; Get collection.
    - list -> `anix.coll.list(page)`; Get recommend list of collections;
    - releases -> `anix.coll.releases(cid, page)`; Get releases in a collection.
    - search -> `anix.coll.search(query, page)`; Finding a collection by name.
    - comments `anix.coll.comments`:
      * get -> `anix.coll.comments.get(cid, page)`; Get collection comments.
      * add -> `anix.coll.comments.add(cid, message, parent_comment_id, reply_to_profile_id, spoiler)`; Add comment to collection.
      * vote -> `anix.coll.comments.vote(ccmid, mark)`; Rate a comment.
      * votes -> `anix.coll.comments.votes(ccmid, page)`; List of rated.
      * replies -> `anix.coll.comments.replies(ccmid, page)`; Responses to a comment.
      * edit -> `anix.coll.comments.edit(ccmid, message, spoiler)`; Edit a comment.
      * delete -> `anix.coll.comments.delete(ccmid)`; Delete a comment.

* Voice -> `anix.voice()`; See all available voiceovers.

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
		* delete
	- comment:
		* get 
		* vote
		* add
	- random

* Collections:
	- my:
		* get
		* create
		* edit
		* delete
	- favorite:
		* get
		* add
		* delete

* Discover:
	- interesting
	- watching
	- discussing
	- comments
	- schedule

* Filter
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
