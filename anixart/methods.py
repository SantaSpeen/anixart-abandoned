# -*- coding: utf-8 -*-

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
BLOCKLIST = "/profile/blocklist/all/{}"  # page

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

# TODO
EDIT_AVATAR = "/profile/preference/avatar/edit"

#############  COLLECTION  #############

# GET
COLLECTION = "/collection/{}"  # collection id
COLLECTION_RELEASES = "/collection/{}/releases/{}"  # collection id / page
COLLECTION_LIST = "/collection/all/{}"  # page

COLLECTION_COMMENTS = "/collection/comment/all/{}/{}"  # collection id / page
COLLECTION_COMMENTS_ADD = "/collection/comment/add/{}"  # collection id req: {"message": msg, "parentCommentId": pcmi, "replyToProfileId": rtpi, "spoiler": false}
COLLECTION_COMMENTS_VOTE = "/collection/comment/vote/{}/{}"  # collection comment id / mark (1, 2)
COLLECTION_COMMENTS_VOTES = "/collection/comment/votes/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_REPLIES = "/collection/comment/replies/{}/{}"  # collection comment id / page
COLLECTION_COMMENTS_EDIT = "/collection/comment/edit/{}"  # collection comment id req: {"message": msg, "spoiler": false}
COLLECTION_COMMENTS_DELETE = "/collection/comment/delete/{}"  # collection comment id

################         ################

WATCHING = "/profile/list/all/1/{}"  # + page
# "/profile/list/all/1796506/1/{}"
IN_PLANS = "/profile/list/all/2/{}"  # + page
WATCHED = "/profile/list/all/3/{}"  # + page
POST_PONED = "/profile/list/all/4/{}"  # + page
THROWN = "/profile/list/all/5/{}"  # + page
HISTORY = "/history/{}"  # + page
FAVORITE = "favorite/all/{}"  # + page

RELEASE = "/release/{}"  # + release id
