# Anixart Profile methods

## **Оглавление класса**

* Профиль:
    * [/profile](#profile) - Получение профиля по User ID.
    * [/profile/login/history/all](#profileloginhistoryall) - Получение истории ников пользователя.
* Чёрный список:
    * [/profile/blocklist/all](#profileblocklistall) - Получение cписка заблокированных вами пользователей.
    * [/profile/blocklist/add](#profileblocklistadd) - Добавление в чёрный список.
    * [/profile/blocklist/remove](#profileblocklistremove) - Удаление из чёрного списка.
* Друзья:
    * [/profile/friend/all]()
    * [/profile/friend/requests/in/last]()
    * [/profile/friend/requests/out/last]()
    * [/profile/friend/request/send]()
    * [/profile/friend/request/remove}]()
* Голосование за релизы:
    * [Как использовать sort](#sort)
    * [/profile/vote/release/voted](#profilevotereleasevoted) - Получение cписка оценённых релизов пользователем
    * [/profile/vote/release/unvoted](#profilevotereleaseunvoted) - Получение cписка своих не оценённых релизов
* Редактирование профиля:
    * [/profile/preference/status/edit]()
    * [/profile/preference/social/edit]()
    * [/profile/preference/avatar/edit]()
    * [/profile/preference/password/change]()

## **Endpoints**
```python
# GET
PROFILE = "/profile/{user_id}"
PROFILE_NICK_HISTORY = "/profile/login/history/all/{user_id}/{page}" 

PROFILE_BLACKLIST = "/profile/blocklist/all/{page}"
PROFILE_BLACKLIST_ADD = "/profile/blocklist/add/{user_id}"
PROFILE_BLACKLIST_REMOVE = "/profile/blocklist/remove/{user_id}"

FRIENDS = "/profile/friend/all/{user_id}/{page}" # TODO
FRIENDS_RQ_IN = "/profile/friend/requests/in/last"  # TODO
FRIENDS_RQ_OUT = "/profile/friend/requests/out/last"  # TODO
FRIENDS_SEND = "/profile/friend/request/send/{user_id}" # TODO
# FRIENDS_REMOVE = "/profile/friend/request/remove/{user_id}"   # TODO

VOTE_VOTED = "/profile/vote/release/voted/{}/{}"  # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}"  # page

EDIT_PASSWORD = "/profile/preference/password/change"  # TODO

# POST
EDIT_STATUS = "/profile/preference/status/edit"  # TODO
EDIT_SOCIAL = "/profile/preference/social/edit"  # TODO
EDIT_AVATAR = "/profile/preference/avatar/edit"  # TODO
```
## Profile info

### **/profile**

Метод для получения информации о профиль по User ID

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * User ID: <span style="color:#0060ff">int</span>
    * Пример: `GET {API_URL}/profile/{User ID}`
* Ответ:
    * Тип: json
    * Res: 
```json
  {"code": 0, 
  "profile": {
        "id": 1, 
        "login": "Anixart",
        "avatar": "https://i.imgur.com/YPrxlVv.jpg", 
        "status": "Официальный аккаунт", 
        "sponsorshipExpires": 0, 
        "history": [], 
        "votes": [], 
        "last_activity_time": 0, 
        "register_date": 0, 
        "vk_page": "", 
        "tg_page": "", 
        "inst_page": "", 
        "tt_page": "", 
        "ban_expires": 0, 
        "ban_reason": null, 
        "ban_note": null, 
        "privilege_level": 1, 
        "watching_count": 0, 
        "plan_count": 0, 
        "completed_count": 0, 
        "hold_on_count": 0, 
        "dropped_count": 0, 
        "favorite_count": 0, 
        "comment_count": 0, 
        "collection_count": 0,
        "friend_count": 0, 
        "is_private": false, 
        "is_sponsor": false, 
        "is_banned": false, 
        "is_perm_banned": false, 
        "is_bookmarks_transferred": false, 
        "is_sponsor_transferred": false, 
        "is_vk_bound": false, 
        "is_google_bound": false, 
        "is_episode_notifications_enabled": false, 
        "is_first_episode_notification_enabled": false, 
        "is_comment_notifications_enabled": false, 
        "is_my_collection_comment_notifications_enabled": false, 
        "is_verified": true, 
        "watch_dynamics": [], 
        "friend_status": null, 
        "rating_score": 99, 
        "is_blocked": false, 
        "is_me_blocked": false, 
        "is_stats_hidden": true, 
        "is_counts_hidden": true, 
        "is_social_hidden": true, 
        "is_friend_requests_disallowed": true,
        "is_online": false, 
        "roles": []
      }, 
  "is_my_profile": false}
```

### **/profile/login/history/all**

Метод для получения истории ников пользователя.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * User ID: <span style="color:#0060ff">int</span>
            * Page: <span style="color:#0060ff">int</span>
    * Пример: `GET {API_URL}/profile/login/history/all{User ID}/{Page}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "content": [
    {
      "@id": 1, 
      "id": 177984, 
      "newLogin": "New login", 
      "timestamp": 1624562531
    }, {
      "@id": 2, 
      "id": 177983, 
      "newLogin": "Register login",
      "timestamp": 0
    }
  ], 
  "total_count": 2, 
  "total_page_count": 0, 
  "current_page": 0}
```

## Blacklist

### **/profile/blocklist/all**

Метод для получения cписка заблокированных вами пользователей.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * Page: <span style="color:#0060ff">int</span>
        * params - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
    * Пример: `GET {API_URL}/profile/blocklist/all/{Page}?token={token}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "content": [
    {
      "login": "login", 
      "avatar": "https://static.anixart.tv/avatars/file.jpg", 
      "id": 1, 
      "added_date": 1642683977, 
      "is_verified": false, 
      "is_online": false, 
      "is_sponsor": false
    }
  ], 
  "total_count": 1,
  "total_page_count": 0, 
  "current_page": 0
}
```

### **/profile/blocklist/add**

Метод для добавления пользователя в чёрный список по User ID.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * User ID: <span style="color:#0060ff">int</span>
        * params - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
    * Пример: `GET {API_URL}/profile/blocklist/add/{User ID}?token={token}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
	"code": 0
}
```

### **/profile/blocklist/remove**

Метод для удаления пользователя из чёрного списка по User ID.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * User ID: <span style="color:#0060ff">int</span>
        * params - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
    * Пример: `GET {API_URL}/profile/blocklist/remove/{User ID}?token={token}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
	"code": 0
}
```

## **Friends**

## **Vote**

##### Как использовать sort
    1 -> Сначала последние 
    2 -> Сначала старые 
    3 -> 5 Звёзд 
    4 -> 4 Звёзды
    5 -> 3 Звёзды
    6 -> 2 Звёзды
    7 -> 1 Звезда

### **/profile/vote/release/voted**

Метод для получения cписка оценённых релизов пользователем.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * Page: <span style="color:#0060ff">int</span>
        * params - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
            * sort: <span style="color:#0060ff">int</span>, [подробнее](#sort)
    * Пример: `GET {API_URL}/profile/vote/release/voted/{User ID}/{Page}?sort={sort}&token={token}`
* Ответ:
    * Тип: json
    * Res: ` `

### **/profile/vote/release/unvoted**
    
Метод для получения cписка своих не оценённых релизов.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо: 
        * patch - строка запроса.
            * Page: <span style="color:#0060ff">int</span>
        * params - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
            * sort: <span style="color:#0060ff">int</span>, [подробнее](#sort)
    * Пример: `GET {API_URL}/profile/vote/release/unvoted/{Page}??sort={sort}&token={token}`
* Ответ:
    * Тип: json
    * Res: ` `

## Preference