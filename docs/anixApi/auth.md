# Anixart Auth methods

## Класс ещё не описан!

## **Оглавление класса**

* [/auth/signUp](#authsignup), Для регистрации аккаунта.
* [/auth/verify](#authverify), Для подтверждения регистрации аккаунта.
* [/auth/signIn](#authsignin), Для входа в аккаунт.
* [/auth/firebase](#authfirebase), Для <_err_found_data>

## **Endpoints**

```python
################   AUTH   ################

# POST
SING_UP = "/auth/signUp"
SING_UP_VERIFY = "/auth/verify"
SING_IN = "/auth/signIn"
FIREBASE = "/auth/firebase"
```

## **Auth**

### **/auth/signUp**

Метод для регистрации аккаунта. <br />
После использования этого метода нужно подтвердить почту методом [/auth/verify](#authverify).

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
      * Необходимо:
          * Data - Данные запроса:
              * login: <span style="color:#f1c232">str</span>
              * password: <span style="color:#f1c232">str</span>
              * email: <span style="color:#f1c232">str</span>
    * Пример: `POST {API_URL}/auth/signUp}`
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

### **/auth/verify**

Метод для подтверждения регистрации аккаунта.

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
    * Необходимо: 
        * Data - Данные запроса:
            * code: <span style="color:#0060ff">int</span>, код, поступивший на почту.
            * login: <span style="color:#f1c232">str</span>
            * password: <span style="color:#f1c232">str</span>
            * email: <span style="color:#f1c232">str</span>
            * hash: <span style="color:#f1c232">str</span>, передаётся в ответе от [/auth/signUp](#authsignup)
    * Пример: `POST {API_URL}/auth/signUp}`
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
### **/auth/signIn**

Метод для входа в аккаунт.

* Обращение:
    * Протокол: <span style="color:#02e400">POST</span>
    * Необходимо: 
        * Data - Данные запроса:
            * login: <span style="color:#f1c232">str</span>
            * password: <span style="color:#f1c232">str</span>
    * Пример: `POST {API_URL}/auth/signIn}`
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

### **/auth/firebase**

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
Интересный факт, приложение после авторизации сразу же посылает /auth/firebase.
<br>А при первом открытии:
```
POST /v1/projects/anime-ad-eb8b3/installations HTTP/1.1
Host: firebaseinstallations.googleapis.com
Content-Type: application/json
Accept: application/json
Content-Encoding: gzip
Cache-Control: no-cache
X-Android-Package: com.swiftsoft.anixartd
x-firebase-client: kotlin/1.5.10 android-target-sdk/30 device-brand/samsung fire-fst/22.1.2 fire-core/19.5.0 device-name/b70abab fire-iid/21.1.0 device-model/a70q fire-android/30 android-installer/com.google.android.packageinstaller android-min-sdk/21 fire-fcm/20.1.7_1p android-platform/ fire-installations/16.3.5 fire-auth/20.0.4
x-firebase-client-log-type: 3
X-Android-Cert: 61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81
x-goog-api-key: AIzaSyBFPckWOsp0MEqb_1gwszvM1ILdUixM-uw
User-Agent: Dalvik/2.1.0 (Linux; U; Android 10; SM-A705FN Build/10)
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 140
        
{
	"fid": "dsVzIpPOQE-2lGUlSee_DX",
	"appId": "1:983926366374:android:86c070d43af9c4cd0b5467",
	"authVersion": "FIS_v2",
	"sdkVersion": "a:16.3.5"
}
```