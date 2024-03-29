# Anixart API 

## Список доступных классов:

1. [Auth](methods/auth/)
2. [Profile](methods/profile/#_1) <span style="color:#f1c232">Класс описан частично.</span>
3. [Collection](methods/collections/) <span style="color:red">Класс не описан.</span>
4. [Release](methods/release/) <span style="color:red">Класс не описан.</span>
5. [Other](methods/other/)

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
SING_UP = None
SING_UP_VERIFY = None
SING_IN = None
FIREBASE = None

# Not Cheked
# POST
AUTH_RESEND = None
AUTH_RESTORE = None
AUTH_RESTORE_RESEND = None
AUTH_RESTORE_VERIFY = None
AUTH_SING_IN_WITH_GOOGLE = None
AUTH_SING_IN_WITH_VK = None

################ PROFILE ################
# TODO PROFILE: SETTINGS, SETTINGS_RELEASE, SETTINGS_RELEASE_FIRST,
#  SETTINGS_COMMENTS, SETTINGS_COLLECTION, EDIT_AVATAR, SETTINGS_RELEASE_LIST,
#  SETTINGS_RELEASE_TYPE

# GET
PROFILE = "/profile/{}"  # + profile id
PROFILE_NICK_HISTORY = "/profile/login/history/all/{}/{}"  # profile id / page

PROFILE_BLACKLIST = "/profile/blocklist/all/{}"  # page
PROFILE_BLACKLIST_ADD = "/profile/blocklist/add/{}"  # profile id
PROFILE_BLACKLIST_REMOVE = "/profile/blocklist/remove/{}"  # profile id

FRIENDS = "/profile/friend/all/{}/{}"  # profile id / page
FRIENDS_RQ_IN = "/profile/friend/requests/in/{}"  # page
FRIENDS_RQ_OUT = "/profile/friend/requests/out/{}"  # page
FRIENDS_RQ_IN_LAST = "/profile/friend/requests/in/last"
FRIENDS_RQ_OUT_LAST = "/profile/friend/requests/out/last"
FRIENDS_SEND = "/profile/friend/request/send/{}"  # profile id
FRIENDS_REMOVE = "/profile/friend/request/remove/{}"  # profile id

VOTE_VOTED = "/profile/vote/release/voted/{}/{}"  # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}"  # page

LISTS = "/profile/list/all/{}/{}/{}"  # profile id / list id / page

SETTINGS_NOTIFICATION = "/profile/preference/notification/my"
SETTINGS_NOTIFICATION_RELEASE = "/profile/preference/notification/episode/edit"
SETTINGS_NOTIFICATION_RELEASE_FIRST = "/profile/preference/notification/episode/first/edit"
SETTINGS_NOTIFICATION_COMMENTS = "/profile/preference/notification/comment/edit"
SETTINGS_NOTIFICATION_COLLECTION = "/profile/preference/notification/my/collection/comment/edit"

CHANGE_PASSWORD = "/profile/preference/password/change"

# POST
EDIT_STATUS = "/profile/preference/status/edit"
EDIT_SOCIAL = "/profile/preference/social/edit"
EDIT_AVATAR = "/profile/preference/avatar/edit"

SETTINGS_NOTIFICATION_RELEASE_LIST = "/profile/preference/notification/status/edit"  # {"profileStatusNotificationPreferences":[0 - favorite, + all in AnixList]}
SETTINGS_NOTIFICATION_RELEASE_TYPE = "/profile/preference/notification/type/edit"  # {"profileTypeNotificationPreferences":[type ids]}

# Not Checked
# GET
PROFILE_SOCIAL = "/profile/social/{}"  # profile id

FRIENDS_RECOMENDATION = "/profile/friend/recommendations"
FRIENDS_RQ_HIDE = "profile/friend/request/hide/{}"  # profile id

SETTINGS_PROFILE = "/profile/preference/my"
SETTINGS_PROFILE_CHANGE_EMAIL = "/profile/preference/email/change"  # {current_password, current, new}
SETTINGS_PROFILE_CHANGE_EMAIL_CONFIRM = "/profile/preference/email/change/confirm"  # {current}

# /profile/preference/social
SETTINGS_PROFILE_STATUS_DELETE = "/profile/preference/status/delete"

# POST
PROFILE_PROCESS = "/profile/process/{}"  # profile id

SETTINGS_PROFILE_CHANGE_LOGIN = "/profile/preference/email/login/confirm"  # {login}
SETTINGS_PROFILE_CHANGE_LOGIN_INFO = "/profile/preference/email/login/info"  # {login}

SETTINGS_PROFILE_BIND_GOOGLE = "/profile/preference/google/bind"  # {idToken, }
SETTINGS_PROFILE_UNBIND_GOOGLE = "/profile/preference/google/unbind"
SETTINGS_PROFILE_BIND_VK = "/profile/preference/google/bind"  # {accessToken, }
SETTINGS_PROFILE_UNBIND_VK = "/profile/preference/google/unbind"

SETTINGS_PROFILE_PRIVACY_COUNTS = "/profile/preference/privacy/counts/edit"
SETTINGS_PROFILE_PRIVACY_FRIENDS_REQUESTS = "/profile/preference/privacy/friendRequests/edit"
SETTINGS_PROFILE_PRIVACY_SOCIAL = "/profile/preference/privacy/social/edit"
SETTINGS_PROFILE_PRIVACY_STATS = "/profile/preference/privacy/stats/edit"

#############  COLLECTION  #############

# GET
COLLECTION = "/collection/{}"  # collection id
COLLECTION_RELEASES = "/collection/{}/releases/{}"  # collection id / page
COLLECTION_LIST = "/collection/all/{}"  # page

COLLECTION_COMMENTS = "/collection/comment/all/{}/{}"  # collection id / page
COLLECTION_COMMENTS_VOTE = "/collection/comment/vote/{}/{}"  # collection comment id / mark (1, 2)
COLLECTION_COMMENTS_VOTES = "/collection/comment/votes/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_DELETE = "/collection/comment/delete/{}"  # collection comment id

COLLECTION_FAVORITE = "/collectionFavorite/all/{}"  # page
COLLECTION_FAVORITE_ADD = "/collectionFavorite/add/{}"  # collection id
COLLECTION_FAVORITE_DELETE = "/collectionFavorite/delete/{}"  # collection id

# POST
COLLECTION_COMMENTS_ADD = "/collection/comment/add/{}"  # collection id
COLLECTION_COMMENTS_EDIT = "/collection/comment/edit/{}"  # collection comment id
COLLECTION_COMMENTS_REPLIES = "/collection/comment/replies/{}/{}"  # collection comment id / page

# Not Checked
# GET
COLLECTION_PROFILE = "/collection/all/profile/{}/{}"  # p_id/page
COLLECTION_RELEASE_IN = "/collection/all/release/{}/{}"  # r_id/page

COLLECTION_MY = "/collectionMy/{id}/releases"
COLLECTION_MY_DELETE = "/collectionMy/delete/{}"  # collectionId
COLLECTION_MY_ADD_RELEASE = "/collectionMy/release/add/{}"  # collectionId

# POST
COLLECTION_COMMENTS_PROCESS = "/collection/comment/process/{}"  # commentId
COLLECTION_COMMENTS_REPORT = "/collection/comment/report/{}"  # commentId

COLLECTION_REPORT = "/collection/report/{}"  # collectionId

COLLECTION_MY_CREATE = "/collectionMy/create"
COLLECTION_MY_EDIT = "/collectionMy/edit/{}"  # collectionId
COLLECTION_MY_EDIT_IMAGE = "/collectionMy/editImage/{}"  # collectionId

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

# Not Cheked
# GET
RELEASE_COMMENTS_REPORT = "/release/comment/report/{}"  # commentId
RELEASE_COMMENTS_PROCESS = "/release/comment/process/{}"  # commentId

RELEASE_PROFILE_COMMENTS = "/release/comment/all/profile/{}/{}"  # p_id/page

RELEASE_STREAMING_PLATFORM = "/release/streaming/platform/{}/"  # releaseId

# POST
RELEASE_REPORT = "/release/report/{}"  # r_id

#############    OTHER    #############
# TODO OTHER: EXPORT_BOOKMARKS, IMPORT_BOOKMARKS, CAN_IMPORT_BOOKMARKS

# GET
TYPE = "/type/all"
TYPE_RELEASE = "/type/{}"  # r_id
TOGGLES = "/config/toggles?version_code={}&is_beta={}"  # version_code: int, is_beta: bool
SCHEDULE = "/schedule"

# POST
EXPORT_BOOKMARKS = "/export/bookmarks"  # {"bookmarksExportProfileLists":[0 - favorite, + all in AnixList]}
IMPORT_BOOKMARKS = "/import/bookmarks"  # {"completed":[],"dropped":[],"holdOn":[],"plans":[],"watching":[],"selected_importer_name":"Shikimori"}
CAN_IMPORT_BOOKMARKS = "/import/status"  # code: 0 - Yes, code: 2 - no

# Not Checked
# GET
FILTER = "/filter/{}"  # page {token, genres: [], studio, category, status, year, episodes, sort, country, season, duration, ratings: [], extended_mode: bool}
RELATED = "related/{}/{}"  # relatedId/page

# POST
VIDEO_PARSE = "/video/parse"

#############    SEARCH    #############
# TODO SEARCH: *

# { "query": text, "searchBy": 0}
# POST
SEARCH_COLLECTION = "/search/collections/{}"  # page
SEARCH_RELEASE = "/search/releases/{}"  # page
SEARCH_FAVORITE = "/search/favorites/{}"  # page
SEARCH_COLLECTION_FAVORITE = "/search/favoriteCollections/{}"  # page
SEARCH_LIST = "/search/profile/list/{}/{}"  # list id / page
SEARCH_PROFILE = "/search/profiles/{}"  # page
SEARCH_HISTORY = "/search/history/{}"  # page

# 
SEARCH_COLLECTION_PROFILE = "/search/profileCollections/{}/{}"  # p_id/page

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

NOTIFICATION_COLLECTION_COMMENTS_DELETE = "/notification/collectionComment/delete/{}"  # n_id
NOTIFICATION_MY_COLLECTION_COMMENTS_DELETE = "/notification/my/collection/comment/delete/{}"  # page
NOTIFICATION_RELEASE_COMMENTS_DELETE = "/notification/releaseComment/delete/{}"  # page
NOTIFICATION_EPISODES_DELETE = "/notification/episode/delete/{}"  # page
NOTIFICATION_FRIEND_DELETE = "/notification/friends/delete/{}"  # page

#############    DISCOVER    #############
# TODO DISCOVER: *

# Not Cheked
# POST
DISCOVER_COMMENTS = "/discover/comments"
DISCOVER_DISCUSSING = "/discover/discussing"  # {token}
DISCOVER_INTERESTING = "/discover/interesting"
DISCOVER_RECOMENDATION = "/discover/recommendations/{}"  # page
DISCOVER_WATCING = "/discover/watching/{}"  # page

#############    EpisodeApi.kt    #############
# TODO EpisodeApi.kt: *

# Ой, я заебался, я спать..
# Здесь методы из com.swiftsoft.anixartd.network.api.EpisodeApi
# Если надо, переделай так как тебе надо

# Not Checked
# GET
# @GET("episode/target/{releaseId}/{sourceId}/{position}")
# @GET("episode/{releaseId}/{typeId}/{sourceId}")
# @GET("episode/{releaseId}")
# @GET("episode/updates/{releaseId}/{page}")

# POST
# @POST("episode/report/{releaseId}/{sourceId}/{position}")
# @POST("episode/unwatch/{releaseId}/{sourceId}/{position}")
# @POST("episode/unwatch/{releaseId}/{sourceId}")
# @POST("episode/watch/{releaseId}/{sourceId}/{position}")
# @POST("episode/watch/{releaseId}/{sourceId}")

#############    FAVORITE    #############
# TODO FAVORITE: *

# Not Checked
# GET
FAVORITE = "/favorite/all/{}"  # r_id
FAVORITE_ADD = "/favorite/add/{}"  # r_id
FAVORITE_DELETE = "/favorite/delete/{}"  # r_id {sort}

#############    HISTORY    #############
# TODO HISTORY: *

# GET
HISTORY = "/history/{}"  # page

# Not Checked
# GET
HISTORY_ADD = "/history/add/{}/{}/{}"  # r_id/s_id/position
HISTORY_DELETE = "/history/delete/{}"  # r_id

```