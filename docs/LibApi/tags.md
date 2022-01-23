## **Метки**

* Поддерживаемы API.
    - <span style="color:#7CD9B4">●</span> - <span style="color:#7CD9B4">**_anixart_**</span>
    - <span style="color:#F36374">●</span> - <span style="color:#F36374">**_aniu_**</span>
* Класс документации.
    - <span style="color:blue">●</span> - <span style="color:blue">**_[login](/LibApi/methods/#me)_**</span>
    - <span style="color:blue">●</span> - <span style="color:blue">**_[auth](/LibApi/methods/#auth)_**</span>
    - <span style="color:blue">●</span> - <span style="color:blue">**_[profile](/LibApi/methods/#profile)_**</span>
    - <span style="color:blue">●</span> - <span style="color:blue">**_[collections](/LibApi/methods/#collections)_**</span>
    - <span style="color:blue">●</span> - <span style="color:blue">**_[release](/LibApi/methods/#release)_**</span>
    - <span style="color:blue">●</span> - <span style="color:blue">**_[other](/LibApi/methods/#other)_**</span>

## **Условные обозначения**
1. **uid** - _int_; User Id, _**default**_: `anix.me.get_id()`
2. **rid** - _int_; Release Id.
3. **cid** - _int_; Collection id.
4. **ccmid** - _int_; Collection comment id.
5. **rcmid** - _int_; Release comment id.
6. **page** - _int_; Страница данных, **_default_**: 0.
7. **query** - _str_; Текст поиска.
8. **message** - _str_; Текст комментария.
9. **spoiler** - _bool_; Является ли комментарий спойлером, **_default_**: False.
10. **mark** - _int_; Оценка комментария. Используйте `AnixComment.UP` или `AnixComment.DOWN`
11. **rmark** - _int_; Оценка аниме релиза. От 1 до 10.

```
from anixart import AnixComment

...
mark = AnixComment.UP
anix.coll.comments.vote(ccmid, mark)
```
