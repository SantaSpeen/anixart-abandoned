from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount()
anix_user.id = 12345
anix_user.token = "token"
anix = AnixAPI(anix_user)

v = anix.other.voice()

for i in v['types']:
    # vid = voiceover id
    print(f"[vid: {i['id']}] Voiceover: \"{i['name']}\"")
