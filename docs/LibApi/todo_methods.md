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