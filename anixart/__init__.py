# -*- coding: utf-8 -*-

# ╔═══╗╔═╗ ╔╗╔══╗╔═╗╔═╗╔═══╗╔═══╗╔════╗
# ║╔═╗║║║╚╗║║╚╣─╝╚╗╚╝╔╝║╔═╗║║╔═╗║║╔╗╔╗║
# ║║ ║║║╔╗╚╝║ ║║  ╚╗╔╝ ║║ ║║║╚═╝║╚╝║║╚╝
# ║╚═╝║║║╚╗║║ ║║  ╔╝╚╗ ║╚═╝║║╔╗╔╝  ║║
# ║╔═╗║║║ ║║║╔╣─╗╔╝╔╗╚╗║╔═╗║║║║╚╗  ║║
# ╚╝ ╚╝╚╝ ╚═╝╚══╝╚═╝╚═╝╚╝ ╚╝╚╝╚═╝  ╚╝

"""
Non-official Anixart API wrapper.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapper for using the anixart API, the best application for watching anime in the CIS countries. 
From myself I can say that the library was created for informational purposes only. 
I do not advise you to do such things as cheat likes,have respect for the project. 
If complaints are received from the project administration, then access to the repository will be limited.

Usage:
~~~~~~

>>> from anixart import AnixUserAccount, AnixAPI
>>> anix_user = AnixUserAccount("login", "password")
>>> anix = AnixAPI(anix_user)
>>> me = anix.profile.get()
>>> print(me)
"""
from .__version__ import __license__, __description__
from .__version__ import __version__, __url__, __build__, __title__, __author__, __author_email__, __copyright__

from .api import AnixUserAccount, AnixAPI
from .endpoints import AnixComment, AnixProfileVotedSort, AnixList


def check_update():
    import requests
    secret = "721b36f6e91e82ca6599222515f441cf8b2bc9bcfa7e10980e4e45d38286a2e4"
    url = "http://santaspeen.ru:81/api/anixart/version.last?v=1.0"
    try:
        r = requests.get(url, headers={"anixart-secret": secret}).json()
        print(r)
        if not r['object']['is_last']:
            last_version = r['object']['last_version'][0]
            version = r['object']['version'][0]
            print(f"Found new version: {last_version}!!\n"
                  f"Installed version: {version}.")
            ans = input("Do you need update Anixart API lib (y/n): ")
            if ans.lower() == "y":
                print("\nUpdating Anixart API lib.\n")
                import os
                print("$ pip3 install -U anixart")
                os.system("pip3 install -U anixart")
                print("\n\n"
                      "Anixart API lib updated..\n"
                      "Reload script!\n")
                exit(0)
            else:
                print("Abort.")
        else:
            print("Your Anixart API lib has last version.")
    except requests.exceptions.ConnectionError:
        print("Can not connect to santaspeen api.")
        del requests
