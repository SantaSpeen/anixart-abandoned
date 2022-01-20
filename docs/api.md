# API библиотеки

<span style="color:red">**Отображение некоторых списков может быть некорректным**.</span>

Некторые разделы дублируются на https://aniu.ru/, такие разделы будут помечены как `aniu`

**Все эндпоинты можно найти здесь:** [тык](https://github.com/SantaSpeen/anixart/blob/master/anixart/methods.py "тык")

## **Условные обозначения**
1. **uid** - _int_; User Id, _**default**_: `anix.me.get_id()`
2. **rid** - _int_; Release Id.
3. **cid** - _int_; Collection id.
4. **ccmid** - _int_; Collection comment id.
4. **rcmid** - _int_; Release comment id.
5. **page** - _int_; Страница данных, **_default_**: 0.
6. **query** - _str_; Текст поиска.
7. **message** - _str_; Текст комментария.
8. **spoiler** - _bool_; Является ли комментарий спойлером, **_default_**: False.
9. **mark** - _int_; Оценка комментария. Используйте `AnixComment.UP` или `AnixComment.DOWN`
```
from anixart import AnixComment

...
mark = AnixComment.UP
anix.coll.comments.vote(ccmid, mark)
```
10. rmark - _int_; Оценка аниме релиза. От 1 до 10.
## **Доступные методы**

### Me
**Класс с данными для входа.** 

Базовый класс -> `anix.me`

* login -> `anix.me.get_login()`
* password -> `anix.me.get_password()`
* token -> `anix.me.get_token()`
* id -> `anix.me.get_id()`

### Auth
**Класс для авторизации.** 

Базовый класс -> `anix.auth`

- Sing In -> `anix.auth.sing_in()`; **Не используйте этот метод.** Библиотека сама входит в аккаунт.
- Sing Up -> `anix.auth.sing_up()`; **Не используйте этот метод.** Библиотека сама регистрирует аккаунт.
- Firebase -> `anix.auth.firebase()`; 
- Change password -> `anix.auth.change_password(old_pass, new_pass)`; Смена пароля.

### Profile
**Класс для работы с профилями.** 

Базовый класс -> `anix.profile`

- get -> `anix.profile.get(uid)`; Получить профиль по uid.
- history -> `anix.profile.history(uid, page)`; Получить историю никнеймов пользователя.
- blocklist  -> `anix.profile.blocklist(page)`; Получить свой чёрный список.
- friends `anix.profile.friends`: 
     * get -> `anix.profile.friends.get(uid, page)`; Получить список друзей по uid.
     * incoming -> `anix.profile.friends.incoming()`; Получить входящие заявки в друзья.
     * outgoing -> `anix.profile.friends.outgoing()`; Получить исходящие заявки в друзья.
     * add -> `anix.profile.friends.add(uid)`; Подписаться на пользователя. **uid обязателен.** 
     * accept -> `anix.profile.friends.accept(uid)`; Принять заявку в друзья. **uid обязателен.**
     * remove -> `anix.profile.friends.remove(uid)`; Удалить пользователя из друзей. **uid обязателен.**
- vote `anix.profile.vote`: 
     * voted -> `anix.profile.vote.voted(uid, page)`; Получить список оценённых аниме. 
     * unvoted -> `anix.profile.vote.unvoted(page)`; Получить не список оценённых аниме. 
- edit `anix.profile.edit`: 
     * status -> `anix.profile.edit.status(text)`; Отредактировать статус.
     * social -> `anix.profile.edit.social(instId, tgId, vkId, ttId)`; Отредактировать контакты.

### Collections
**Класс для работы с коллекциями** 

`aniu`

Базовый класс -> `anix.collection`, также можно использовать `anix.coll`.

- get -> `anix.coll.get(cid)`; Получить коллекцию по cid.
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
  
  
### Release
**Класс для работы с релизами (аниме)**

_Местами_ `aniu` 

Базовый класс -> `anix.release`

- get -> `anix.release.get(rid)`; Получить релиз по rid.
- random -> `anix.release.random()`; Получить рандомный релиз.
- vote:
     * add -> `anix.release.get(rid, rmark)`; Установить оценку релизу.
     * delete ->`anix.release.get(rid)`; Удалить свою оценку у релиза.
- comments `anix.release.comments`:
     * get -> `anix.release.comments.get(cid, page)`; Get release comments.
     * add -> `anix.release.comments.add(cid, message, parent_comment_id, reply_to_profile_id, spoiler)`; Add comment to release.
     * vote -> `anix.release.comments.vote(rcmid, mark)`; Rate a comment.
     * votes -> `anix.release.comments.votes(rcmid, page)`; List of rated.
     * replies -> `anix.release.comments.replies(rcmid, page)`; Responses to a comment.
     * edit -> `anix.release.comments.edit(rcmid, message, spoiler)`; Edit a comment.
     * delete -> `anix.release.comments.delete(rcmid)`; Delete a comment.

### Other
**Класс для работы с остальными методами** 

Базовый класс -> `anix.other`

- voice -> `anix.other.voice()`; Получить список всех возможных озвучек.

## **Ещё не описанные методы**

### Profile
- list:
     * get:
          * watching
          * plan
          * watched
          * postponed
          * thrown
          * history           
          * favorite 
          * collections
     * add
- edit:
    * avatar
    * notification:
         * episode
         * comment
         * status
         * collection

### Collections:
- my:
     * get
     * create
     * edit
     * delete
- favorite:
     * get
     * add
     * delete

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
    
### Notification
Ещё не изучал.
