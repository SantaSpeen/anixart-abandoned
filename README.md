# anix_api - Anixart API project. (non-offical)

### Use:
```python3
from anix_api import AnixAuth, AnixUserAccount, AnixAPI

user = AnixUserAccount(login="##", password="##")
anix = AnixAPI(user)
print(f"Token: {anix.user.get_token()}; ID: {anix.user.get_id()}")
```

### Ready now:
* Auth:
	1. Sing in