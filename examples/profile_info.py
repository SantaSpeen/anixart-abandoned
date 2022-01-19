from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)

uid = 1785853  # If None, program use self uid.

profile = anix.profile.get(uid)['profile']
nick = profile.get('login')
uid = profile.get('id')
status = profile.get('status')

print(f"UID: {uid}\n"
      f"Nick: {nick}\n"
      f"Status: {status}")

print("\nNick history:")
profile_nick_history = anix.profile.history(uid)
if profile_nick_history['total_count'] > 0:
    for h in profile_nick_history['content']:
        print(f"{h['@id']}. {h['newLogin']}")
else:
    print("No nick history.")

print("\nUsers friends:")
profile_friends = anix.profile.friends.get(uid)
if profile_friends['total_count'] > 0:
    for f in profile_friends['content']:
        print(f"UID: {f['id']}; Nick: {f['login']}; Is online: {f['is_online']}")
else:
    print("User has no friends.")

