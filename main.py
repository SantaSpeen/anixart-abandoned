from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount("login", "password")
anix = AnixAPI(anix_user)


def main(uid):
    profile = anix.profile.get(uid)['profile']
    if profile is None:
        print("Id is incorrect")
        return

    nick = profile.get('login', )
    uid = profile.get('id', )
    status = profile.get('status', )
    vk = profile.get('vk_page', )
    tg = profile.get('tg_page', )
    inst = profile.get('inst_page', )
    tt = profile.get('tt_page', )
    reg_date = profile.get('register_date', )

    print(
        f"\nNick: {nick}\n" +
        f"Id: {uid}\n" +
        f"Status: {status}\n" +
        f"Vk: {vk}\n" +
        f"Tg: {tg}\n" +
        f"Inst: {inst}\n" +
        f"Tt: {tt}\n" +
        f"Register date: {reg_date}\n"
    )


if __name__ == '__main__':
    uid = input("Type anixart user id: ")
    if uid == "":
        uid = None
    main(uid)
