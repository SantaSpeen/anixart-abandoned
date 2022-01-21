# anixart
#### Non-official Anixart API wrapper. 
![Magic](https://img.shields.io/badge/Made%20with-Magic-orange?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyBpZD0iQ2FwYV8xIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHdpZHRoPSI1MTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGc+PHBhdGggZD0ibTM5NS44MiAxODIuNjE2LTE4OC43MiAxODguNzItMTIuOTEgMS43Mi05LjM1IDIwLjU0LTM0LjMxIDM0LjMxLTExLjAxLS43My0xMS4yNSAyMi45OS01Ni40OCA1Ni40OGMtMi45MyAyLjkzLTYuNzcgNC4zOS0xMC42MSA0LjM5cy03LjY4LTEuNDYtMTAuNjEtNC4zOWwtMjIuNjItMjIuNjJoLS4wMWwtMjIuNjItMjIuNjNjLTUuODYtNS44Ni01Ljg2LTE1LjM2IDAtMjEuMjJsNzcuNjMtNzcuNjMgMTYuNi03LjAzIDUuNjYtMTUuMjMgMzQuMzEtMzQuMzEgMTQuODQtNC45MiA3LjQyLTE3LjM0IDE2Ny41Ny0xNjcuNTcgMzMuMjQgMzMuMjR6IiBmaWxsPSIjZjY2Ii8+PHBhdGggZD0ibTM5NS44MiAxMTYuMTQ2djY2LjQ3bC0xODguNzIgMTg4LjcyLTEyLjkxIDEuNzItOS4zNSAyMC41NC0zNC4zMSAzNC4zMS0xMS4wMS0uNzMtMTEuMjUgMjIuOTktNTYuNDggNTYuNDhjLTIuOTMgMi45My02Ljc3IDQuMzktMTAuNjEgNC4zOXMtNy42OC0xLjQ2LTEwLjYxLTQuMzlsLTIyLjYyLTIyLjYyIDMzNC42NC0zMzQuNjR6IiBmaWxsPSIjZTYyZTZiIi8+PHBhdGggZD0ibTUwNi42MSAyMDkuMDA2LTY5LjE0LTY5LjEzIDQzLjA1LTg4LjM4YzIuOC01Ljc1IDEuNjUtMTIuNjUtMi44OC0xNy4xNy00LjUyLTQuNTMtMTEuNDItNS42OC0xNy4xNy0yLjg4bC04OC4zOCA0My4wNS02OS4xMy02OS4xNGMtNC4zNS00LjM1LTEwLjkyLTUuNi0xNi41Ni0zLjE2LTUuNjUgMi40NS05LjIzIDguMDktOS4wNCAxNC4yNGwyLjg2IDkwLjQ1LTg1LjM3IDU3LjgzYy00LjkxIDMuMzItNy40IDkuMjItNi4zNiAxNS4wNCAxLjA0IDUuODMgNS40IDEwLjUxIDExLjE1IDExLjk0bDk2LjYyIDI0LjAxIDI0LjAxIDk2LjYyYzEuNDMgNS43NSA2LjExIDEwLjExIDExLjk0IDExLjE1Ljg3LjE2IDEuNzUuMjMgMi42Mi4yMyA0LjkyIDAgOS42LTIuNDIgMTIuNDItNi41OWw1Ny44My04NS4zNyA5MC40NSAyLjg2YzYuMTQuMTkgMTEuNzktMy4zOSAxNC4yNC05LjA0IDIuNDQtNS42NCAxLjE5LTEyLjIxLTMuMTYtMTYuNTZ6IiBmaWxsPSIjZmFiZTJjIi8+PHBhdGggZD0ibTI5Ni4yNiAyMTUuNzA2IDI0LjAxIDk2LjYyYzEuNDMgNS43NSA2LjExIDEwLjExIDExLjk0IDExLjE1Ljg3LjE2IDEuNzUuMjMgMi42Mi4yMyA0LjkyIDAgOS42LTIuNDIgMTIuNDItNi41OWw1Ny44My04NS4zNyA5MC40NSAyLjg2YzYuMTQuMTkgMTEuNzktMy4zOSAxNC4yNC05LjA0IDIuNDQtNS42NCAxLjE5LTEyLjIxLTMuMTYtMTYuNTZsLTY5LjE0LTY5LjEzIDQzLjA1LTg4LjM4YzIuOC01Ljc1IDEuNjUtMTIuNjUtMi44OC0xNy4xN3oiIGZpbGw9IiNmZDkwMjUiLz48cGF0aCBkPSJtNDY1IDQxNi45NjZjLTI1LjkyIDAtNDcgMjEuMDgtNDcgNDdzMjEuMDggNDcgNDcgNDcgNDctMjEuMDggNDctNDctMjEuMDgtNDctNDctNDd6IiBmaWxsPSIjZmFiZTJjIi8+PHBhdGggZD0ibTEwNCAyOC45NjZoLTEzdi0xM2MwLTguMjg0LTYuNzE2LTE1LTE1LTE1cy0xNSA2LjcxNi0xNSAxNXYxM2gtMTNjLTguMjg0IDAtMTUgNi43MTYtMTUgMTVzNi43MTYgMTUgMTUgMTVoMTN2MTNjMCA4LjI4NCA2LjcxNiAxNSAxNSAxNXMxNS02LjcxNiAxNS0xNXYtMTNoMTNjOC4yODQgMCAxNS02LjcxNiAxNS0xNXMtNi43MTYtMTUtMTUtMTV6IiBmaWxsPSIjZmVkODQzIi8+PHBhdGggZD0ibTIwNy4xIDM3MS4zMzYtMjIuMjYgMjIuMjYtNDUuMzItODcuNjIgMjIuMjYtMjIuMjZ6IiBmaWxsPSIjZmVkODQzIi8+PHBhdGggZD0ibTE4NC44NCAzOTMuNTk2IDIyLjI2LTIyLjI2LTIyLjY2LTQzLjgxLTIyLjI2NSAyMi4yNjV6IiBmaWxsPSIjZmFiZTJjIi8+PHBhdGggZD0ibTE1MC41MyA0MjcuOTA2LTIyLjI2IDIyLjI2LTQ1LjMyLTg3LjYyIDIyLjI2LTIyLjI2eiIgZmlsbD0iI2ZlZDg0MyIvPjxwYXRoIGQ9Im0xMjguMjcgNDUwLjE2NiAyMi4yNi0yMi4yNi0yMi42NTUtNDMuODE1LTIyLjI2IDIyLjI2eiIgZmlsbD0iI2ZhYmUyYyIvPjxjaXJjbGUgY3g9IjE1IiBjeT0iMTE5Ljk2OSIgZmlsbD0iIzVlZDhkMyIgcj0iMTUiLz48Y2lyY2xlIGN4PSIxMjgiIGN5PSIxOTkuOTY5IiBmaWxsPSIjZDU5OWVkIiByPSIxNSIvPjxjaXJjbGUgY3g9IjE5MiIgY3k9IjYzLjk2NCIgZmlsbD0iI2Y2NiIgcj0iMTUiLz48Y2lyY2xlIGN4PSIzMjgiIGN5PSI0MTUuOTY3IiBmaWxsPSIjMzFiZWJlIiByPSIxNSIvPjxjaXJjbGUgY3g9IjQ0MCIgY3k9IjMyNy45NjciIGZpbGw9IiNhZDc3ZTMiIHI9IjE0Ljk5OSIvPjwvZz48L3N2Zz4=)


[![PyPi version](https://badgen.net/pypi/v/anixart/)](https://pypi.com/project/anixart)
[![PyPI license](https://img.shields.io/pypi/l/anixart.svg)](https://pypi.python.org/pypi/anixart/)
[![GitHub commits](https://img.shields.io/github/commits-since/SantaSpeen/anixart/0.3.4.svg)](https://GitHub.com/SantaSpeen/anixart/commit/)
[![Documentation Status](https://readthedocs.org/projects/anixart/badge/?version=latest)](https://anixart.readthedocs.io/?badge=latest)

Pip:

[![PyPI download month](https://img.shields.io/pypi/dm/anixart.svg)](https://pypi.python.org/pypi/anixart/)
[![PyPI download week](https://img.shields.io/pypi/dd/anixart.svg)](https://pypi.python.org/pypi/anixart/)



**Документация на русском:** [ТЫК](https://anixart.readthedocs.io/ "тык")

* Description:
    * **EN**: Wrapper for using the anixart API, the best application for watching anime in the CIS countries. From myself I can say that the library was created for informational purposes only. I do not advise you to do such things as cheat likes,have respect for the project. If complaints are received from the project administration, then access to the repository will be limited.
    * **RU**: Враппер для использования anixart API, наилучшего приложения для просмотра аниме на территории стран СНГ.  От себя могу сказать, что библиотека создана лишь для ознакомления. Не советую заниматься такимим вещами как накрутка лайков, имейте уважение к проекту. Если поступят жалобы от администрации проекта, то доступ к репозиторию будет ограничен.


* Endpoints: [here](https://github.com/SantaSpeen/anixart/blob/master/anixart/endpoints.py)
* Contacts: [Vk](https://vk.com/l.vindeta "Vk"), [Tg](https://t.me/id01234 "Tg").

### Install:

Via pip:

* `pip install -U anixart`

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

* Release
  - get -> `anix.release.get(rid)`; Get release rid.
  - random -> `anix.release.random()`; Get random release.
  - vote:
      * add -> `anix.release.get(rid, rmark)`; Set mark.
      * delete ->`anix.release.get(rid)`; Del mark.
  - comments `anix.release.comments`:
    * get -> `anix.release.comments.get(cid, page)`; Get release comments.
    * add -> `anix.release.comments.add(cid, message, parent_comment_id, reply_to_profile_id, spoiler)`; Add comment to release.
    * vote -> `anix.release.comments.vote(rcmid, mark)`; Rate a comment.
    * votes -> `anix.release.comments.votes(rcmid, page)`; List of rated.
    * replies -> `anix.release.comments.replies(rcmid, page)`; Responses to a comment.
    * edit -> `anix.release.comments.edit(rcmid, message, spoiler)`; Edit a comment.
    * delete -> `anix.release.comments.delete(rcmid)`; Delete a comment.

* Other `anix.other`:
  - type -> `anix.other.type()`; See all available voiceovers.

### **In plans:**

### Profile
- list:
     * add
```python
# GET
PROFILE_BLACKLIST_ADD = "/profile/blocklist/add/{}"  # profile id
PROFILE_BLACKLIST_REMOVE = "/profile/blocklist/remove/{}"  # profile id

LISTS = "/profile/list/all/{}/{}/{}"  # profile id / list id / page

SETTINGS_NOTIFICATION = "/profile/preference/notification/my"
SETTINGS_RELEASE_NOTIFICATION = "/profile/preference/notification/episode/edit"
SETTINGS_RELEASE_FIRST_NOTIFICATION = "/profile/preference/notification/episode/first/edit"
SETTINGS_COMMENTS_NOTIFICATION = "/profile/preference/notification/comment/edit"
SETTINGS_COLLECTION_NOTIFICATION = "/profile/preference/notification/my/collection/comment/edit"
```

### Collections:
- my:
     * get
     * create
     * edit
     * delete
```python
# GET
COLLECTION_FAVORITE = "/collectionFavorite/all/{}"  # page
COLLECTION_FAVORITE_ADD = "/collectionFavorite/add/{}"  # collection id
COLLECTION_FAVORITE_DELETE = "/collectionFavorite/delete/{}"  # collection id
```

### Discover
- interesting
- watching
- discussing
- comments
- schedule

### Filter
- get

### Episode
- get: 
     * voice
     * player
     * video
- set:
     * watch
     * unwatch

### Search
```python
# data: { "query": text, "searchBy": 0}

# POST
COLLECTION_SEARCH = "/search/collections/{}"  # page
RELEASE_SEARCH = "/search/releases/{}"  # page
FAVORITE_SEARCH = "/search/favorites/{}"  # page
COLLECTION_SEARCH_FAVORITE = "/search/favoriteCollections/{}"  # page
LIST_SEARCH = "/search/profile/list/{}/{}"  # list id / page
PROFILE_SEARCH = "/search/profiles/{}"  # page
HISTORY_SEARCH = "/search/history/{}"  # page
```

### Notification
```python
# GET
NOTIFICATION_READ = "/notification/read"
NOTIFICATION_COUNT = "/notification/count"
NOTIFICATION_COLLECTION_COMMENTS = "/notification/collectionComments/{}"  # page
NOTIFICATION_MY_COLLECTION_COMMENTS = "/notification/my/collection/comments/{}"  # page
NOTIFICATION_RELEASE_COMMENTS = "/notification/releaseComments/{}"  # page
NOTIFICATION_EPISODES = "/notification/episodes/{}"  # page
NOTIFICATION_FRIEND = "/notification/friends/{}"  # page
```

### Other
```python
# GET
HISTORY = "/history/{}"  # page
TOGGLES = "/config/toggles?version_code={}&is_beta={}"  # version_code: int, is_beta: bool

# POST
EXPORT_BOOKMARKS = "/export/bookmarks"  # {"bookmarksExportProfileLists":[0 - favorite, + all in AnixList]}
IMPORT_BOOKMARKS = "/import/bookmarks"  # {"completed":[],"dropped":[],"holdOn":[],"plans":[],"watching":[],"selected_importer_name":"Shikimori"}
CAN_IMPORT_BOOKMARKS = "/import/status"  # code: 0 - Yes, code: 2 - no

```