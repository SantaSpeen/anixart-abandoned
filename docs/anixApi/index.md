# Anixart API 

## Список доступных классов:

1. [Auth](/anixApi/auth/) <span style="color:red">Класс не описан.</span>
2. [Profile](/anixApi/profile/#_1) <span style="color:#f1c232">Класс описан частично.</span>
3. [Collection](/anixApi/collections/) <span style="color:red">Класс не описан.</span>
4. [Release](/anixApi/release/) <span style="color:red">Класс не описан.</span>
5. [Other](/anixApi/other/)

## endpoints.py

```python
# -*- coding: utf-8 -*-

class AnixComment:
    DOWN = 1
    UP = 2


class AnixProfileVotedSort:
    LAST_FIRST = 1
    OLD_FIRST = 2
    STAR_5 = 3
    STAR_4 = 4
    STAR_3 = 5
    STAR_2 = 6
    STAR_1 = 7


API_URL = "https://api.anixart.tv"

################   AUTH   ################

# POST
SING_UP = "/auth/signUp"
SING_UP_VERIFY = "/auth/verify"
SING_IN = "/auth/signIn"
FIREBASE = "/auth/firebase"

# GET
CHANGE_PASSWORD = "/profile/preference/password/change"

################ PROFILE ################

# GET
PROFILE = "/profile/{}"  # + profile id
PROFILE_NICK_HISTORY = "/profile/login/history/all/{}/{}"  # profile id / page

PROFILE_BLACKLIST = "/profile/blocklist/all/{}"  # page
PROFILE_BLACKLIST_ADD = "/profile/blocklist/add/{}"  # profile id #TODO
PROFILE_BLACKLIST_REMOVE = "/profile/blocklist/remove/{}"  # profile id #TODO

FRIENDS = "/profile/friend/all/{}/{}"  # profile id / page
FRIENDS_RQ_IN = "/profile/friend/requests/in/last"
FRIENDS_RQ_OUT = "/profile/friend/requests/out/last"
FRIENDS_SEND = "/profile/friend/request/send/{}"  # profile id
FRIENDS_REMOVE = "/profile/friend/request/remove/{}"  # profile id

VOTE_VOTED = "/profile/vote/release/voted/{}/{}"  # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}"  # page

# POST
EDIT_STATUS = "/profile/preference/status/edit"
EDIT_SOCIAL = "/profile/preference/social/edit"
EDIT_AVATAR = "/profile/preference/avatar/edit"  # TODO

#############  COLLECTION  #############

# GET
COLLECTION = "/collection/{}"  # collection id
COLLECTION_RELEASES = "/collection/{}/releases/{}"  # collection id / page
COLLECTION_LIST = "/collection/all/{}"  # page

COLLECTION_COMMENTS = "/collection/comment/all/{}/{}"  # collection id / page
COLLECTION_COMMENTS_VOTE = "/collection/comment/vote/{}/{}"  # collection comment id / mark (1, 2)
COLLECTION_COMMENTS_VOTES = "/collection/comment/votes/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_REPLIES = "/collection/comment/replies/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_DELETE = "/collection/comment/delete/{}"  # collection comment id

# POST
COLLECTION_SEARCH = "/search/collections/{}"  # page req: { "query": text, "searchBy": 0}

COLLECTION_COMMENTS_ADD = "/collection/comment/add/{}"  # collection id
COLLECTION_COMMENTS_EDIT = "/collection/comment/edit/{}"  # collection comment id

#############    RELEASE    #############

# GET
RELEASE = "/release/{}"  # release id
RELEASE_VOTE_ADD = "/release/vote/add/{}/{}"  # release id / mark 1-5
RELEASE_VOTE_DELETE = "/release/vote/delete/{}"  # release id
RELEASE_RANDOM = "/release/random"

RELEASE_COMMENTS = "/release/comment/all/{}/{}"  # release id / page
RELEASE_COMMENTS_VOTE = "/release/comment/vote/{}/{}"  # release comment id / mark (1, 2)
RELEASE_COMMENTS_VOTES = "/release/comment/votes/{}/{}"  # release comment id / page
RELEASE_COMMENTS_REPLIES = "/release/comment/replies/{}/{}"  # release comment id / page
RELEASE_COMMENTS_DELETE = "/release/comment/delete/{}"  # release comment id

# POST
RELEASE_COMMENTS_ADD = "/release/comment/add/{}"  # release id
RELEASE_COMMENTS_EDIT = "/release/comment/edit/{}"  # release comment id

#############    OTHER    #############

# GET
VOICE = "/type/all"

# TODO
# WATCHING = "/profile/list/all/1/{}"  # + page
# # "/profile/list/all/1796506/1/{}"
# IN_PLANS = "/profile/list/all/2/{}"  # + page
# WATCHED = "/profile/list/all/3/{}"  # + page
# POSTPONED = "/profile/list/all/4/{}"  # + page
# THROWN = "/profile/list/all/5/{}"  # + page
# HISTORY = "/history/{}"  # + page
# FAVORITE = "favorite/all/{}"  # + page
```