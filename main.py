from anix_api import AnixUserAccount, AnixAPI

user = AnixUserAccount("##", "##")
anix = AnixAPI(user)
print(f"Token: {anix.user.get_token()}; ID: {anix.user.get_id()}")
