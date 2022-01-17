from anix_api import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("rewrwerwfwef", "APIPassword")
anix = AnixAPI(anix_user)
print(f"Token: {anix.me.get_token()}; ID: {anix.me.get_id()}")