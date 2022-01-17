from anix_api import AnixAuth, AnixUserAccount, AnixAPI

user = AnixUserAccount(login="SanitAni", password="MaximPassword")
anix = AnixAPI(user)
anix.auth.sing_in()
print(f"Token: {anix.user.get_token()}; ID: {anix.user.get_id()}")

