---
hide:
  - toc
---
# Anixart API wrapper
## Установка

Используя pip:

* `pip install -U anixart`

## Использование:

```python3
from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

profile = anix.profile.get()
print(profile['profile'])
```