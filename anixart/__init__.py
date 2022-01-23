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

version_secret = "65f1c508f136b74025215a95a1e551bc5261b4dfb68258465db34d7cd666464a"
based_on = 21101018


def check_update():
    import requests
    url = "http://santaspeen.ru:81/api/anixart/version.last?v=1.0"
    try:
        r = requests.get(url, headers={"anixart-secret": version_secret}).json()
        if r.get("error"):
            print(r.get("error"))
            return

        if not r['object']['is_last']:

            from . import endpoints
            url2 = endpoints.API_URL + endpoints.TOGGLES.format(based_on, False)
            r2 = requests.get(url2, headers={'User-Agent': f'AnixartAPI/1.0-{based_on} ()'}).json()

            last_version = r['object']['last_version'][0]
            version = r['object']['version'][0]
            last_anixart_version = r2['lastVersionCode']
            print(f"Found new version: {last_version}!!\n"
                  f"Installed version: {version}.\n"
                  f"Anixart App last build: {last_anixart_version}\n")

            print("$ pip3 install -U anixart")
            ans = input("Do you need update Anixart API lib (y/n): ")

            if ans.lower() == "y":
                print("\nUpdating Anixart API lib.\n")
                import os
                os.system("pip3 install -U anixart")
                print("\n\n"
                      "Anixart API lib updated..\n"
                      "Reload script!\n")
                exit(0)

            else:
                print("Abort.")
        else:
            print("Your Anixart API lib has last version.")
            del requests
    except requests.exceptions.ConnectionError:
        print("Can not connect to santaspeen api.")
