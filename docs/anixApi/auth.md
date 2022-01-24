# Anixart Auth methods

## Класс ещё не описан!

## **Оглавление класса**

* [Метод убран по просьбе администратора проекта.](#authsignup), Для регистрации аккаунта.
* [Метод убран по просьбе администратора проекта.](#authverify), Для подтверждения регистрации аккаунта.
* [Метод убран по просьбе администратора проекта.](#authsignin), Для входа в аккаунт.
* [Метод убран по просьбе администратора проекта.](#authfirebase), Для <_err_found_data>

## **Endpoints**

```python
################   AUTH   ################

# POST
SING_UP = "Метод убран по просьбе администратора проекта."
SING_UP_VERIFY = "Метод убран по просьбе администратора проекта."
SING_IN = "Метод убран по просьбе администратора проекта."
FIREBASE = "Метод убран по просьбе администратора проекта."
```

## **Auth**

### **Метод убран по просьбе администратора проекта.**

Метод для регистрации аккаунта. <br />
После использования этого метода нужно подтвердить почту методом [Метод убран по просьбе администратора проекта.](#authverify).

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
      * Необходимо:
          * Data - Данные запроса:
              * login: <span style="color:#f1c232">str</span>
              * password: <span style="color:#f1c232">str</span>
              * email: <span style="color:#f1c232">str</span>
    * Пример: `POST Метод убран по просьбе администратора проекта.}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "hash": "hash string", 
  "codeTimestampExpires": 1642752174
}
```

### **Метод убран по просьбе администратора проекта.**

Метод для подтверждения регистрации аккаунта.

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
    * Необходимо: 
        * Data - Данные запроса:
            * code: <span style="color:#0060ff">int</span>, код, поступивший на почту.
            * login: <span style="color:#f1c232">str</span>
            * password: <span style="color:#f1c232">str</span>
            * email: <span style="color:#f1c232">str</span>
            * hash: <span style="color:#f1c232">str</span>, передаётся в ответе от [Метод убран по просьбе администратора проекта.](#authsignup)
    * Пример: `POST Метод убран по просьбе администратора проекта.}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "profile": 
  {
    "id": 1234567, 
    "login": "login string", 
    "avatar": "https://static.anixart.tv/avatars/no_avatar.jpg", 
    "status": "", 
    "sponsorshipExpires": 0, 
    "history": [], 
    "votes": [], 
    "last_activity_time": 0, 
    "register_date": 1234567890, 
    "vk_page": "", 
    "tg_page": "", 
    "inst_page": "", 
    "tt_page": "", 
    "ban_expires": 0, 
    "ban_reason": null, 
    "ban_note": null, 
    "privilege_level": 0, 
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
    "is_verified": false, 
    "watch_dynamics": [], 
    "friend_status": null, 
    "rating_score": 0, 
    "is_blocked": false, 
    "is_me_blocked": false, 
    "is_stats_hidden": false, 
    "is_counts_hidden": false, 
    "is_social_hidden": false, 
    "is_friend_requests_disallowed": false,
    "is_online": false, 
    "roles": []
  }, 
  "profileToken": 
  {
    "id": 1234567, 
    "token": "token sting"
  }
}
```
### **Метод убран по просьбе администратора проекта.**

Метод для входа в аккаунт.

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
    * Необходимо: 
        * Data - Данные запроса:
            * login: <span style="color:#f1c232">str</span>
            * password: <span style="color:#f1c232">str</span>
    * Пример: `POST Метод убран по просьбе администратора проекта.}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "profile": 
  {
    "id": "login string", 
    "login": "st", 
    "avatar": "https://static.anixart.tv/avatars/no_avatar.jpg", 
    "status": "", 
    "sponsorshipExpires": 0, 
    "history": [], "votes": [], 
    "last_activity_time": 1642756487, 
    "register_date": 1642752760, 
    ...
  }, 
  "profileToken": {
    "id": 1234567, 
    "token": "token sting"
  }
}

```

### **Метод убран по просьбе администратора проекта.**

Метод для <_err_found_data>

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
    * Необходимо: 
        * Data - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
    * Пример: `POST {API_URL}/auth/firebase}`
* Ответ:
    * Тип: json
    * Res: 
```json
{
  "code": 0, 
  "topicName": "<_err_found_data> string"
}
```
Интересный факт, приложение после авторизации сразу же посылает Метод убран по просьбе администратора проекта..
<br>А при первом открытии:
```
Метод убран по просьбе администратора проекта.
```