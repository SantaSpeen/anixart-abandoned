# anix_api - Anixart API project. (non-offical)

### Use:
```python3
from anix_api import AnixUserAccount, AnixAPI

user = AnixUserAccount(login="", password="", need_reg=False, mail="your@mail.tv")
anix = AnixAPI(user)
print(f"Token: {anix.user.get_token()}; ID: {anix.user.get_id()}")
```

### Ready now:
* Auth:
	- Sing In -> 
	```python3 
	from anix_api import AnixUserAccount, AnixAPI

	user = AnixUserAccount("login", "password" )
	anix = AnixAPI(user)
	
	# anix.auth.sing_in()  -> Do not use this metod. Programm auto singing in.
	```
	- Sing Up ->
	```python3 
	from anix_api import AnixUserAccount, AnixAPI

	user = AnixUserAccount("login", "password", need_reg=True, mail="your@mail.tv")
	anix = AnixAPI(user)
	
	# anix.auth.sing_up()  -> Do not use this metod. Programm auto singing up.
	```
	- Firebase ->
	```python3 
	from anix_api import AnixUserAccount, AnixAPI

	user = AnixUserAccount("login", "password" )
	anix = AnixAPI(user)
	
	fb = anix.auth.firebase()
	print(fb)
	```