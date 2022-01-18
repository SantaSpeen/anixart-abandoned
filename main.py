from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("rewrwerwfwef", "APIPassword")
anix = AnixAPI(anix_user)

print(f"Token: {anix.me.get_token()}; ID: {anix.me.get_id()}")

profile = anix.profile.get()['profile']
nick = profile['login']
status = profile['status']
vk = profile['vk_page']
tg = profile['tg_page']
inst = profile['inst_page']
tt = profile['tt_page']
reg_date = profile['register_date']

print(f"Nick: {nick}\nStatus: {status}\nVk: {vk}\nTg: {tg}\nInst: {inst}\nTt: {tt}\nRegister date: {reg_date}")