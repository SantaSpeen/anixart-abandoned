## Методы:


### Me
**Класс с данными для входа.** 

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:blue">**_login_**</span>

Базовый класс -> `anix.me`

* <span style="color:#7CD9B4">●</span> login -> `anix.me.get_login()`
* <span style="color:#7CD9B4">●</span> password -> `anix.me.get_password()`
* <span style="color:#7CD9B4">●</span> token -> `anix.me.get_token()`
* <span style="color:#7CD9B4">●</span> id -> `anix.me.get_id()`

### Auth
**Класс для авторизации.** 

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:blue">**_auth_**</span>

Базовый класс -> `anix.auth`

- <span style="color:#7CD9B4">●</span> Sing In -> `anix.auth.sing_in()`; **Не используйте этот метод.** Библиотека сама входит в аккаунт.
- <span style="color:#7CD9B4">●</span> Sing Up -> `anix.auth.sing_up()`; **Не используйте этот метод.** Библиотека сама регистрирует аккаунт.
- <span style="color:#7CD9B4">●</span> Firebase -> `anix.auth.firebase()`; 
- <span style="color:#7CD9B4">●</span> Change password -> `anix.auth.change_password(old_pass, new_pass)`; Смена пароля.

### Profile
**Класс для работы с профилями.** 

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:blue">**_profile_**</span>

Базовый класс -> `anix.profile`

- <span style="color:#7CD9B4">●</span> get -> `anix.profile.get(uid)`; Получить профиль по uid.
- <span style="color:#7CD9B4">●</span> history -> `anix.profile.history(uid, page)`; Получить историю никнеймов пользователя.
- <span style="color:#7CD9B4">●</span> blocklist  -> `anix.profile.blocklist(page)`; Получить свой чёрный список.
- <span style="color:#7CD9B4">●</span> friends `anix.profile.friends`: 
     * get -> `anix.profile.friends.get(uid, page)`; Получить список друзей по uid.
     * incoming -> `anix.profile.friends.incoming()`; Получить входящие заявки в друзья.
     * outgoing -> `anix.profile.friends.outgoing()`; Получить исходящие заявки в друзья.
     * add -> `anix.profile.friends.add(uid)`; Подписаться на пользователя. **uid обязателен.** 
     * accept -> `anix.profile.friends.accept(uid)`; Принять заявку в друзья. **uid обязателен.**
     * remove -> `anix.profile.friends.remove(uid)`; Удалить пользователя из друзей. **uid обязателен.**
- <span style="color:#7CD9B4">●</span> vote `anix.profile.vote`: 
     * voted -> `anix.profile.vote.voted(uid, page)`; Получить список оценённых аниме. 
     * unvoted -> `anix.profile.vote.unvoted(page)`; Получить не список оценённых аниме. 
- <span style="color:#7CD9B4">●</span> edit `anix.profile.edit`: 
     * status -> `anix.profile.edit.status(text)`; Отредактировать статус.
     * social -> `anix.profile.edit.social(instId, tgId, vkId, ttId)`; Отредактировать контакты.

### Collections
**Класс для работы с коллекциями** 

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:#F36374">**_aniu_**</span>, <span style="color:blue">**_collections_**</span>

Базовый класс -> `anix.collection`, также можно использовать `anix.coll`.

- <span style="color:#7CD9B4">●</span> <span style="color:#F36374">●</span> get -> `anix.coll.get(cid)`; Получить коллекцию по cid.
- <span style="color:#7CD9B4">●</span> list -> `anix.coll.list(page)`; Get recommend list of collections;
- <span style="color:#7CD9B4">●</span> <span style="color:#F36374">●</span> releases -> `anix.coll.releases(cid, page)`; Get releases in a collection.
- <span style="color:#7CD9B4">●</span> <span style="color:#F36374">●</span> search -> `anix.coll.search(query, page)`; Finding a collection by name.
- <span style="color:#7CD9B4">●</span> comments `anix.coll.comments`:
     * get -> `anix.coll.comments.get(cid, page)`; Get collection comments.
     * add -> `anix.coll.comments.add(cid, message, parent_comment_id, reply_to_profile_id, spoiler)`; Add comment to collection.
     * vote -> `anix.coll.comments.vote(ccmid, mark)`; Rate a comment.
     * votes -> `anix.coll.comments.votes(ccmid, page)`; List of rated.
     * replies -> `anix.coll.comments.replies(ccmid, page)`; Responses to a comment.
     * edit -> `anix.coll.comments.edit(ccmid, message, spoiler)`; Edit a comment.
     * delete -> `anix.coll.comments.delete(ccmid)`; Delete a comment.
  
  
### Release
**Класс для работы с релизами (аниме)**

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:#F36374">**_aniu_**</span><span style="color:red">¹</span>, <span style="color:blue">**_release_**</span>
<br>
<span style="color:red">¹**Обратите внимание**</span>, на _**aniu**_ rid не всегда совпадает с rid на **_anixart_**.

Базовый класс -> `anix.release`

- <span style="color:#7CD9B4">●</span> <span style="color:#F36374">●</span> get -> `anix.release.get(rid)`; Получить релиз по rid.
- <span style="color:#7CD9B4">●</span> random -> `anix.release.random()`; Получить рандомный релиз.
- <span style="color:#7CD9B4">●</span> vote:
     * add -> `anix.release.get(rid, rmark)`; Установить оценку релизу.
     * delete ->`anix.release.get(rid)`; Удалить свою оценку у релиза.
- <span style="color:#7CD9B4">●</span> comments `anix.release.comments`:
     * get -> `anix.release.comments.get(cid, page)`; Get release comments.
     * add -> `anix.release.comments.add(cid, message, parent_comment_id, reply_to_profile_id, spoiler)`; Add comment to release.
     * vote -> `anix.release.comments.vote(rcmid, mark)`; Rate a comment.
     * votes -> `anix.release.comments.votes(rcmid, page)`; List of rated.
     * replies -> `anix.release.comments.replies(rcmid, page)`; Responses to a comment.
     * edit -> `anix.release.comments.edit(rcmid, message, spoiler)`; Edit a comment.
     * delete -> `anix.release.comments.delete(rcmid)`; Delete a comment.

### Other
**Класс для работы с остальными методами** 

Метки: <span style="color:#7CD9B4">**_anixart_**</span>, <span style="color:blue">**_other_**</span>

Базовый класс -> `anix.other`

- <span style="color:#7CD9B4">●</span> voice -> `anix.other.voice()`; Получить список всех возможных озвучек.
