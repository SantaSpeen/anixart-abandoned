---
hide:
  - toc
---
# API библиотеки

## **Общая информация**

<span style="color:red">**Отображение некоторых списков может быть некорректным**.</span>

**Все эндпоинты можно найти здесь:** [тык](https://github.com/SantaSpeen/anixart/blob/master/anixart/endpoints.py "тык")


## Вспомогательные классы

* В библиотеке используются вспомогательные классы: 
    * `AnixComment`
    * `AnixProfileVotedSort`
    * `AnixList`
```python
from anixart import AnixComment, AnixProfileVotedSort, AnixList
...
anix.profile.list(list_id=AnixList.WATCHED)
...
anix.coll.comments.vote(ccmid, mark=AnixComment.UP)
...
# Для AnixProfileVotedSort ещё нет методов в библиотеке.
```