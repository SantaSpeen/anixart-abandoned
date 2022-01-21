# Anixart API 

## Список доступных классов:

1. [Auth](/anixApi/auth/)
2. [Profile](/anixApi/profile/#_1) <span style="color:#f1c232">Класс описан частично.</span>
3. [Collection](/anixApi/collections/) <span style="color:red">Класс не описан.</span>
4. [Release](/anixApi/release/) <span style="color:red">Класс не описан.</span>
5. [Other](/anixApi/other/)

## Быстрый старт

[API (application programming interface)](https://ru.wikipedia.org/wiki/API) — это посредник между разработчиком приложений и какой-либо средой, с которой это приложение должно взаимодействовать. API упрощает создание кода, поскольку предоставляет набор готовых классов, функций или структур для работы с имеющимися данными.

### Формат запросов

Чтобы обратиться к методу API, нужно выполнить POST или GET запрос вида:

```
https://api.anixart.tv/METHOD?PARAMS&token=TOKEN
```

Он состоит из нескольких частей:


* METHOD (обязательно) — название метода API, к которому вы хотите обратиться. Обратите внимание: имя метода чувствительно к регистру.
* PARAMS (не обязательно) — входные параметры соответствующего метода API, последовательность пар name=value, разделенных амперсандом. Список параметров указан на странице с описанием метода.
* TOKEN (обязательно) — ключ доступа.

#### Разбор запроса

Для получения данных о пользователе с идентификатором `27` необходимо составить запрос такого вида:


`https://api.anixart.tv/profile/1?token=TOKEN`

Рассмотрим отдельно все его составляющие:

* `https://` — протокол соединения,

* `api.anixart.tv` — адрес API-сервиса,

* `/profile` — название метода API,

* `/1` `?token=` — параметры запроса.

В ответ сервер вернет JSON-объект с запрошенными данными (или сообщение об ошибке, если что-то пошло не так). 


## endpoints.py

```python
# -*- coding: utf-8 -*-

class AnixComment:
    DOWN = 1
    UP = 2


class AnixProfileVotedSort:
    LAST_FIRST = 1
    OLD_FIRST = 2
    STAR_5 = 3
    STAR_4 = 4
    STAR_3 = 5
    STAR_2 = 6
    STAR_1 = 7


class AnixList:
    WATCHING = 1
    IN_PLANS = 2
    WATCHED = 3
    POSTPONED = 4
    DROPPED = 5


API_URL = "https://api.anixart.tv"

################   AUTH   ################

# POST
SING_UP = "/auth/signUp"
SING_UP_VERIFY = "/auth/verify"
SING_IN = "/auth/signIn"
FIREBASE = "/auth/firebase"

# GET
CHANGE_PASSWORD = "/profile/preference/password/change"

################ PROFILE ################
# TODO PROFILE: PROFILE_BLACKLIST_ADD, PROFILE_BLACKLIST_REMOVE, LISTS, SETTINGS_NOTIFICATION,
#  SETTINGS_RELEASE_NOTIFICATION, SETTINGS_RELEASE_FIRST_NOTIFICATION, SETTINGS_COMMENTS_NOTIFICATION,
#  SETTINGS_COLLECTION_NOTIFICATION, EDIT_AVATAR, SETTINGS_RELEASE_LIST_NOTIFICATION, SETTINGS_RELEASE_TYPE_NOTIFICATION

# GET
PROFILE = "/profile/{}"  # + profile id
PROFILE_NICK_HISTORY = "/profile/login/history/all/{}/{}"  # profile id / page

PROFILE_BLACKLIST = "/profile/blocklist/all/{}"  # page
PROFILE_BLACKLIST_ADD = "/profile/blocklist/add/{}"  # profile id
PROFILE_BLACKLIST_REMOVE = "/profile/blocklist/remove/{}"  # profile id

FRIENDS = "/profile/friend/all/{}/{}"  # profile id / page
FRIENDS_RQ_IN = "/profile/friend/requests/in/last"
FRIENDS_RQ_OUT = "/profile/friend/requests/out/last"
FRIENDS_SEND = "/profile/friend/request/send/{}"  # profile id
FRIENDS_REMOVE = "/profile/friend/request/remove/{}"  # profile id

VOTE_VOTED = "/profile/vote/release/voted/{}/{}"  # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}"  # page

LISTS = "/profile/list/all/{}/{}/{}"  # profile id / list id / page

SETTINGS_NOTIFICATION = "/profile/preference/notification/my"
SETTINGS_RELEASE_NOTIFICATION = "/profile/preference/notification/episode/edit"
SETTINGS_RELEASE_FIRST_NOTIFICATION = "/profile/preference/notification/episode/first/edit"
SETTINGS_COMMENTS_NOTIFICATION = "/profile/preference/notification/comment/edit"
SETTINGS_COLLECTION_NOTIFICATION = "/profile/preference/notification/my/collection/comment/edit"

# POST
EDIT_STATUS = "/profile/preference/status/edit"
EDIT_SOCIAL = "/profile/preference/social/edit"
EDIT_AVATAR = "/profile/preference/avatar/edit"

SETTINGS_RELEASE_LIST_NOTIFICATION = "/profile/preference/notification/status/edit"  # {"profileStatusNotificationPreferences":[0 - favorite, + all in AnixList]}
SETTINGS_RELEASE_TYPE_NOTIFICATION = "/profile/preference/notification/type/edit"   # {"profileTypeNotificationPreferences":[type ids]}

#############  COLLECTION  #############
# TODO COLLECTION: COLLECTION_FAVORITE, COLLECTION_FAVORITE_ADD, COLLECTION_FAVORITE_DELETE

# GET
COLLECTION = "/collection/{}"  # collection id
COLLECTION_RELEASES = "/collection/{}/releases/{}"  # collection id / page
COLLECTION_LIST = "/collection/all/{}"  # page

COLLECTION_COMMENTS = "/collection/comment/all/{}/{}"  # collection id / page
COLLECTION_COMMENTS_VOTE = "/collection/comment/vote/{}/{}"  # collection comment id / mark (1, 2)
COLLECTION_COMMENTS_VOTES = "/collection/comment/votes/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_REPLIES = "/collection/comment/replies/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_DELETE = "/collection/comment/delete/{}"  # collection comment id

COLLECTION_COMMENTS_ADD = "/collection/comment/add/{}"  # collection id
COLLECTION_COMMENTS_EDIT = "/collection/comment/edit/{}"  # collection comment id

COLLECTION_FAVORITE = "/collectionFavorite/all/{}"  # page
COLLECTION_FAVORITE_ADD = "/collectionFavorite/add/{}"  # collection id
COLLECTION_FAVORITE_DELETE = "/collectionFavorite/delete/{}"  # collection id

#############    RELEASE    #############

# GET
RELEASE = "/release/{}"  # release id
RELEASE_VOTE_ADD = "/release/vote/add/{}/{}"  # release id / mark 1-5
RELEASE_VOTE_DELETE = "/release/vote/delete/{}"  # release id
RELEASE_RANDOM = "/release/random"

RELEASE_COMMENTS = "/release/comment/all/{}/{}"  # release id / page
RELEASE_COMMENTS_VOTE = "/release/comment/vote/{}/{}"  # release comment id / mark (1, 2)
RELEASE_COMMENTS_VOTES = "/release/comment/votes/{}/{}"  # release comment id / page
RELEASE_COMMENTS_REPLIES = "/release/comment/replies/{}/{}"  # release comment id / page
RELEASE_COMMENTS_DELETE = "/release/comment/delete/{}"  # release comment id

# POST
RELEASE_COMMENTS_ADD = "/release/comment/add/{}"  # release id
RELEASE_COMMENTS_EDIT = "/release/comment/edit/{}"  # release comment id

#############    OTHER    #############
# TODO OTHER: HISTORY, TOGGLES, EXPORT_BOOKMARKS, IMPORT_BOOKMARKS, CAN_IMPORT_BOOKMARKS

# GET
TYPE = "/type/all"
HISTORY = "/history/{}"  # page
TOGGLES = "/config/toggles?version_code={}&is_beta={}"  # version_code: int, is_beta: bool

# POST
EXPORT_BOOKMARKS = "/export/bookmarks"  # {"bookmarksExportProfileLists":[0 - favorite, + all in AnixList]}
IMPORT_BOOKMARKS = "/import/bookmarks"  # {"completed":[],"dropped":[],"holdOn":[],"plans":[],"watching":[],"selected_importer_name":"Shikimori"}
CAN_IMPORT_BOOKMARKS = "/import/status"  # code: 0 - Yes, code: 2 - no

#############    SEARCH    #############
# TODO SEARCH: *

# { "query": text, "searchBy": 0}
# POST
COLLECTION_SEARCH = "/search/collections/{}"  # page
RELEASE_SEARCH = "/search/releases/{}"  # page
FAVORITE_SEARCH = "/search/favorites/{}"  # page
COLLECTION_SEARCH_FAVORITE = "/search/favoriteCollections/{}"  # page
LIST_SEARCH = "/search/profile/list/{}/{}"  # list id / page
PROFILE_SEARCH = "/search/profiles/{}"  # page
HISTORY_SEARCH = "/search/history/{}"  # page

#############    NOTIFICATIONS    #############
# TODO NOTIFICATIONS: *

# GET
NOTIFICATION_READ = "/notification/read"
NOTIFICATION_COUNT = "/notification/count"
NOTIFICATION_COLLECTION_COMMENTS = "/notification/collectionComments/{}"  # page
NOTIFICATION_MY_COLLECTION_COMMENTS = "/notification/my/collection/comments/{}"  # page
NOTIFICATION_RELEASE_COMMENTS = "/notification/releaseComments/{}"  # page
NOTIFICATION_EPISODES = "/notification/episodes/{}"  # page
NOTIFICATION_FRIEND = "/notification/friends/{}"  # page

```