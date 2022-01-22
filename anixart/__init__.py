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
