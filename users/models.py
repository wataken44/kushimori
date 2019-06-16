
from google.cloud import firestore

USER_COLLECTION = u'users'
SESSION_COLLECTION = u'sessions'

class UserModel(object):
    def __init__(self, user_id, name, screen_name, email):
        self._user_id = user_id
        self._name = name
        self._screen_name = screen_name
        self._email = email

    # data get/put
    @staticmethod
    def get_collection():
        db = firestore.Client()
        return db.collection(USER_COLLECTION)

    @staticmethod
    def get(user_id):
        ref = UserModel.get_collection().document(user_id).get()
        if not ref.exists:
            return None
        return UserModel.from_dict(ref.to_dict())

    def put(self):
        data = self.to_dict()
        UserModel.get_collection().document(self._user_id).set(data)
        
    @staticmethod
    def from_dict(source):
        user_id = source["user_id"]
        name = source["name"]
        screen_name = source["screen_name"]
        email = source["email"]

        return UserModel(user_id, name, screen_name, email)

    def to_dict(self):
        return {
            "user_id": self._user_id,
            "name": self._name,
            "screen_name": self._screen_name,
            "email": self._email,
        }

    def assign(self, source):
        self.user_id = source["user_id"]
        self.name = source["name"]
        self.screen_name = source["screen_name"]
        self.email = source["email"]

    # properties

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    user_id = property(get_user_id, set_user_id, None, "")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name, None, "")

    def get_screen_name(self):
        return self._screen_name

    def set_screen_name(self, screen_name):
        self._screen_name = screen_name

    screen_name = property(get_screen_name, set_screen_name, None, "")

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    email = property(get_email, set_email, None, "")


class SessionModel(object):
    def __init__(self, session_id, user_id, screen_name, created_at):
        self._session_id = session_id
        self._user_id = user_id
        self._screen_name = screen_name
        self._created_at = created_at


    # data get/put
    @staticmethod
    def get_collection():
        db = firestore.Client()
        return db.collection(SESSION_COLLECTION)

    @staticmethod
    def get(session_id):
        ref = SessionModel.get_collection().document(session_id).get()
        if not ref.exists:
            return None
        return SessionModel.from_dict(ref.to_dict())

    def put(self):
        data = self.to_dict()
        SessionModel.get_collection().document(self._session_id).set(data)

        
    @staticmethod
    def from_dict(source):
        session_id = source["session_id"]
        user_id = source["user_id"]
        screen_name = source["screen_name"]
        created_at = source["created_at"]

        return SessionModel(session_id, user_id, screen_name, created_at)

    def to_dict(self):
        return {
            "session_id": self._session_id,
            "user_id": self._user_id,
            "screen_name": self._screen_name,
            "created_at": self._created_at,
        }

    def assign(self, source):
        self.session_id = source["session_id"]
        self.user_id = source["user_id"]
        self.screen_name = source["screen_name"]
        self.created_at = source["created_at"]

    # properties

    def get_session_id(self):
        return self._session_id

    def set_session_id(self, session_id):
        self._session_id = session_id

    session_id = property(get_session_id, set_session_id, None, "")

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    user_id = property(get_user_id, set_user_id, None, "")

    def get_screen_name(self):
        return self._screen_name

    def set_screen_name(self, screen_name):
        self._screen_name = screen_name

    screen_name = property(get_screen_name, set_screen_name, None, "")

    def get_created_at(self):
        return self._created_at

    def set_created_at(self, created_at):
        self._created_at = created_at

    created_at = property(get_created_at, set_created_at, None, "")
