from anixart import AnixAPI


anix = AnixAPI(anix_user)

#  'code': 9 Кажись бан 10 минутной почты
#  zwoho.com

# uid = 1785853  # If None, program use self uid.
page = 1

profile = anix.profile.blocklist(page)
print(profile)
