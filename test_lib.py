from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("rewrwerwfwef", "APIPassword")
anix = AnixAPI(anix_user)

if __name__ == '__main__':
    v = anix.other.voice()
    print(anix.me.token)
    print(v)
