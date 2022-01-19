from .methods import RELEASE, RELEASE_VOTE_ADD, RELEASE_VOTE_DELETE, RELEASE_RANDOM, RELEASE_COMMENTS_REPLIES, \
    RELEASE_COMMENTS_EDIT, RELEASE_COMMENTS_DELETE, RELEASE_COMMENTS_VOTES, RELEASE_COMMENTS_VOTE, RELEASE_COMMENTS_ADD, \
    RELEASE_COMMENTS

from .request_handler import AnixRequestsHandler


class AnixReleaseBase(AnixRequestsHandler):
    def __init__(self, user):
        super(AnixReleaseBase, self).__init__(user.token)
        self.id = user.id
        self._get = super().get
        self._post = super().post

    def _parse_uid(self, uid):
        if uid is None:
            uid = self.id
        uid = str(uid)
        return uid

    def _parse_args(self, uid, page):
        uid = self._parse_uid(uid)
        page = str(page)
        return [uid, page]


class AnixReleaseComments(AnixReleaseBase):

    def get(self, rid, page=0):
        rid, page = self._parse_args(rid, page)
        return self._get(RELEASE_COMMENTS.format(rid, page)).json()

    def add(self, cid, message, parent_comment_id=None, reply_to_profile_id=None, spoiler=False):
        payload = {"message": message,
                   "parentCommentId": parent_comment_id,
                   "replyToProfileId": reply_to_profile_id,
                   "spoiler": spoiler}
        cid = str(cid)
        return self._post(RELEASE_COMMENTS_ADD.format(cid), payload, True).json()

    def vote(self, rcmid, mark):
        rcmid = str(rcmid)
        mark = str(mark)
        return self._get(RELEASE_COMMENTS_VOTE.format(rcmid, mark)).json()

    def votes(self, rcmid, page=0):
        rcmid = str(rcmid)
        page = str(page)
        return self._get(RELEASE_COMMENTS_VOTES.format(rcmid, page)).json()

    def replies(self, rcmid, page=0):
        rcmid, page = self._parse_args(rcmid, page)
        return self._post(RELEASE_COMMENTS_REPLIES.format(rcmid, page), is_json=True).json()

    def edit(self, rcmid, message, spoiler=False):
        payload = {"message": message,
                   "spoiler": spoiler}
        ccmid = str(rcmid)
        return self._post(RELEASE_COMMENTS_EDIT.format(ccmid), payload, True).json()

    def delete(self, rcmid):
        rcmid = str(rcmid)
        return self._get(RELEASE_COMMENTS_DELETE.format(rcmid)).json()


class AnixReleasesVote(AnixReleaseBase):

    def add(self, rid, mark):
        return self._get(RELEASE_VOTE_ADD.format(rid, mark)).json()

    def delete(self, rid, mark):
        return self._get(RELEASE_VOTE_DELETE.format(rid, mark)).json()


class AnixReleases(AnixReleaseBase):

    def get(self, rid):
        return self._get(RELEASE.format(rid), {'extended_mode': True}).json()

    def random(self):
        return self._get(RELEASE_RANDOM, {'extended_mode': True}).json()


class AnixRelease(AnixReleases):

    def __init__(self, user):
        super(AnixRelease, self).__init__(user)
        self.vote = AnixReleasesVote(user)
        self.comments = AnixReleaseComments(user)
