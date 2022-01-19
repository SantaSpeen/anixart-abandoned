# API библиотеки

**Все эндпоинты можно найти здесь:** [тык](https://github.com/SantaSpeen/anixart/blob/master/anixart/methods.py "тык")

## **Условные обозначения**
1. **uid** - _int_; User Id, _**default**_: `anix.me.get_id()`
2. **page** - _int_; Страница данных, **_default_**: 0.
3. **cid** - _int_; Collection id.
4. **ccmid** - _int_; Collection comment id.
5. **query** - _str_; Текст поиска.
6. **message** - _str_; Текст комментария.
7. **spoiler** - _bool_; Является ли комментарий спойлером, **_default_**: False.
8. **mark** - _int_; Поставить оценку комментарию. Используйте `AnixComment.UP` или `AnixComment.DOWN`
```python
from anixart import AnixComment

...
mark = AnixComment.UP
anix.coll.comments.vote(ccmid, mark)
```
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

- ~~Sing In~~ -> `anix.auth.sing_in()`; **Не используйте этот метод.** Библиотека сама входит в аккаунт.
- ~~Sing Up~~ -> `anix.auth.sing_up()`; **Не используйте этот метод.** Библиотека сама регистрирует аккаунт.
- Firebase -> `anix.auth.firebase()`; 
- Change password -> `anix.auth.change_password(old_pass, new_pass)`; Смена пароля.

### Profile
**Класс для работы с профилями.** 

Базовый класс -> `anix.profile`

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

### Collections
**Класс для работы с коллекциями** 

Базовый класс -> `anix.collection`, также можно использовать `anix.coll`.

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
  
### Other
**Класс для работы с остальными методами** 

Базовый класс -> `anix.other`

- voice -> `anix.other.voice()`; Получить список всех возможных озвучек.

## **Ещё не описанные методы**

### Profile
- list:
  * get:
    - watching
    - plan
    - watched
    - postponed
    - thrown
    - history
    - favorite 
    - collections
  * add
- edit:
    * avatar
    * notification:
        - episode
        - comment
        - status
        - voice (type)
        - collection

### Release
- get
- vote:
    * add
    * delete
- comment:
    * get 
    * vote
    * add
- random

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
  - voice
  - player
  - video
- set:
    - watch
    - unwatch
    
### Notification
Ещё не изучал.
