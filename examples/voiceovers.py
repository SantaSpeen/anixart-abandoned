from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

v = anix.other.voice()

for i in v['types']:
    # vid = voiceover id
    print(f"[vid: {i['id']}] Voiceover: \"{i['name']}\"")
