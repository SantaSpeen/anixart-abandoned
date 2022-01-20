# Примеры

Все примеры находятся в папке [/examples](https://github.com/SantaSpeen/anixart/tree/master/examples) на GitHub.

## Базовый

В этом примере, изменяя `uid` можно получить данные о профиле.

``` python3 title="profile_info.py"
from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

uid = 1

profile = anix.profile.get(uid)['profile']
if profile is None:
    print("Id is incorrect")
    exit(0)

nick = profile.get('login', )
uid = profile.get('id', )
status = profile.get('status', )
vk = profile.get('vk_page', )
tg = profile.get('tg_page', )
inst = profile.get('inst_page', )
tt = profile.get('tt_page', )
reg_date = profile.get('register_date', )

print(
    f"\nNick: {nick}\n" +
    f"Id: {uid}\n" +
    f"Status: {status}\n" +
    f"Vk: {vk}\n" +
    f"Tg: {tg}\n" +
    f"Inst: {inst}\n" +
    f"Tt: {tt}\n" +
    f"Register date: {reg_date}\n"
    )
```

## Время в статусе

```python3 title="time_bot.py"
from anixart import AnixUserAccount, AnixAPI
from datetime import datetime
import time

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

print("\n\nAnixart time bot.")

while True:
	s = "✨ "+ datetime.now().strftime("%H:%M %d/%m/%Y")
	anix.profile.edit.status(s)
	print(f"Status edit: {s}")
	time.sleep(15)

```

## Посмотреть все доступные в приложении озвучки

```python3 title="voiceovers.py"
from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

v = anix.other.voice()

for i in v['types']:
    # vid = voiceover id
    print(f"[vid: {i['id']}] Voiceover: \"{i['name']}\"")
```