# CHANGELOG

## TODOs

* **До конца изучить Anixart API.**
* **Доделать раздел API Anixart в документации.**

## Anixart API Wrapper

### 22.01.2022
#### Version: 0.3.5, Build: 568

* Добавлен класс `anix.profile.blocklist` с методами:
    * get
    * add
    * remove
* Добавлен класс `anix.profile.list` с методами:
    * get
* Добавлен класс `anix.coll.favorite` с методами:
    * get
    * add
    * delete
* В классе `anix.other` были добавлены методы:
    * history
    * toggles
* Метод `anix.profile.blocklist()` перенесён в класс `anix.profile.blocklist` и теперь называется `anix.profile.bl.get(page)`.
* Оптимизирована инициализация классов через `@property`.
* Добавлен `logger`, выводит `DEBUG` информацию.

### 21.01.2022
#### Version: 0.3.4, Build: 519

* Перенёс сессию запросов в `AnixUserAccount`.
* Был более подробно изучен Anixart API.
* Были добавлены эндпоинты.
* Метод `anix.other.voice()` был исправлен на `anix.other.type()`.

### 20.01.2022
#### Version: 0.3.3.1, Build: 509

* Исправил ошибку получения метода `EDIT_AVATAR`
* Добавлена работа с кодами ошибок.

#### Version: 0.3.3, Build: 501

* Был добавлен класс Release, подробнее [тут](LibApi/methods/#release)
* Оптимизированный импорты
* Добавлена документация

## Anixart API Wrapper Docs

### 21.01.2022

#### Version: 0.9.2

* Добавлен раздел API Anixart
* API Anixart:
    * Описан Auth
    * Частично описан Profile
    * Описан Other

### 20.01.2022

#### Version: 0.9.1

* Переработана подача
* Добавлены разделы
* Добавлен CHANGELOG

#### Version: 0.9.0

* Документация создана
* Описаны все известные методы