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


def check_update():
    import requests
    secret = "65f1c508f136b74025215a95a1e551bc5261b4dfb68258465db34d7cd666464a"
    url = "http://mc.santaspeen.ru:81/api/anixart/version.last?v=1.0"
    r = requests.get(url, headers={"anixart-secret": secret}).json()
    if r['object']['is_last']:
        ver = r['object']['last_version']
        print(f"Found new version: {ver}!! Installed version: {__version__}.")
        ans = input("Do you need update Anixart API lib (y/n): ")
        if ans.lower() == "y":
            print("\nUpdating Anixart API lib.\n")
            import os
            os.system("pip3 install -U anixart")
            print("\n\n\nAnixart API lib updated..\nReload script!\n")
        else:
            print("Abort.")


from .api import AnixUserAccount, AnixAPI
from .endpoints import AnixComment, AnixProfileVotedSort, AnixList
