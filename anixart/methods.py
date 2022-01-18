API_URL = "https://api.anixart.tv"

################   AUTH   ################

# POST
SING_UP = "/auth/signUp"
SING_UP_VERIFY = "/auth/verify"
SING_IN = "/auth/signIn"
FIREBASE = "/auth/firebase"


################ PROFILE ################

# GET
PROFILE = "/profile/{}" # + profile id
PROFILE_NICK_HISTORY = "/profile/login/history/all/{}/{}" # profile id / page
BLOCKLIST = "/profile/blocklist/all/{}" # page

FRIENDS =  "/profile/friend/all/{}/{}"# profile id / page
FRIENDS_RQ_IN = "/profile/friend/requests/in/last"
FRIENDS_RQ_OUT = "/profile/friend/requests/out/last"
FRIENDS_SEND = "/profile/friend/request/send/{}" # profile id
FRIENDS_REMOVE = "/profile/friend/request/remove/{}" # profile id

VOTE_VOTED = "/profile/vote/release/voted/{}/{}" # profile id / page
VOTE_UNVOTED = "/profile/vote/release/unvoted/{}" # page

# POST
EDIT_STATUS = "/profile/preference/status/edit"
EDIT_SOCIAL = "/profile/preference/social/edit"

# TODO
EDIT_AVATAR = "/profile/preference/avatar/edit" # TODO


################         ################
 
WATCHING = "/profileList/all/1/{}" # + page
"/profile/list/all/1796506/1/{}"
IN_PLANS = "/profileList/all/2/{}" # + page
WATCHED = "/profileList/all/3/{}" # + page
POST_PONED = "/profileList/all/4/{}" # + page
THROWN = "/profileList/all/5/{}" # + page
HISTORY = "/history/{}" # + page
FAVORITE = "favorite/all/{}"  # + page

RELEASE = "/release/{}" # + release id