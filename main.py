from anix_api import AnixAuth, AnixUserAccount, AnixAPI

user = AnixUserAccount(login="##", password="##")
anix = AnixAPI(user)
print(f"Token: {anix.user.get_token()}; ID: {anix.user.get_id()}")
