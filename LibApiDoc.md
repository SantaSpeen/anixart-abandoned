
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
    - favorite `anix.coll.favorite`:
      * get -> `anix.coll.favorite.get(page)`; Get favorite collection.
      * add -> `anix.coll.favorite.add(cid)`; Add collection to favorite.
      * delete ->`anix.coll.favorite.delete(cid)`; Delete collection from favorite.
  
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
  - history -> `anix.other.history(page)`;  
  - toggles -> `anix.other.toggles(app_ver: int, is_beta: bool)`;


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