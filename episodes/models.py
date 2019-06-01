
import zlib

from google.cloud import firestore

EPISODE_COLLECTION = u'episodes'
EPISODE_TEXT_COLLECTION = u'episode_texts'

class EpisodeModel(object):
    def __init__(self, episode_id, chapter_index, chapter_title, title, url, created_at, updated_at):
        self._episode_id = episode_id
        self._chapter_index = chapter_index
        self._chapter_title = chapter_title
        self._title = title
        self._url = url
        self._created_at = created_at
        self._updated_at = updated_at

        self._changed = False

    # data get/put
    @staticmethod
    def get_collection():
        db = firestore.Client()
        return db.collection(EPISODE_COLLECTION)

    @staticmethod
    def get(episode_id):
        ref = EpisodeModel.get_collection().document(episode_id).get()
        if not ref.exists:
            return None
        return EpisodeModel.from_dict(ref.to_dict())

    def put(self):
        data = self.to_dict()
        EpisodeModel.get_collection().document(self._episode_id).set(data)
        
    @staticmethod
    def from_dict(source):
        episode_id = source["episode_id"]
        chapter_index = source["chapter_index"]
        chapter_title = source["chapter_title"]
        title = source["title"]
        url = source["url"]
        created_at = source["created_at"]
        updated_at = source["updated_at"]

        return EpisodeModel(episode_id, chapter_index, chapter_title, title, url, created_at, updated_at)

    def to_dict(self):
        return {
            "episode_id": self._episode_id,
            "chapter_index": self._chapter_index,
            "chapter_title": self._chapter_title,
            "title": self._title,
            "url": self._url,
            "created_at": self._created_at,
            "updated_at": self._updated_at,
        }

    def assign(self, source):
        self.episode_id = source["episode_id"]
        self.chapter_index = source["chapter_index"]
        self.chapter_title = source["chapter_title"]
        self.title = source["title"]
        self.url = source["url"]
        self.created_at = source["created_at"]
        self.updated_at = source["updated_at"]

    def is_changed(self):
        return self._changed

    # properties

    def get_episode_id(self):
        return self._episode_id

    def set_episode_id(self, episode_id):
        self._changed = self._changed or (self._episode_id != episode_id)
        self._episode_id = episode_id

    episode_id = property(get_episode_id, set_episode_id, None, "")

    def get_chapter_index(self):
        return self._chapter_index

    def set_chapter_index(self, chapter_index):
        self._changed = self._changed or (self._chapter_index != chapter_index)
        self._chapter_index = chapter_index

    chapter_index = property(get_chapter_index, set_chapter_index, None, "")

    def get_chapter_title(self):
        return self._chapter_title

    def set_chapter_title(self, chapter_title):
        self._changed = self._changed or (self._chapter_title != chapter_title)
        self._chapter_title = chapter_title

    chapter_title = property(get_chapter_title, set_chapter_title, None, "")

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._changed = self._changed or (self._title != title)
        self._title = title

    title = property(get_title, set_title, None, "")

    def get_url(self):
        return self._url

    def set_url(self, url):
        self._changed = self._changed or (self._url != url)
        self._url = url

    url = property(get_url, set_url, None, "")

    def get_created_at(self):
        return self._created_at

    def set_created_at(self, created_at):
        self._changed = self._changed or (self._created_at != created_at)
        self._created_at = created_at

    created_at = property(get_created_at, set_created_at, None, "")

    def get_updated_at(self):
        return self._updated_at

    def set_updated_at(self, updated_at):
        self._changed = self._changed or (self._updated_at != updated_at)
        self._updated_at = updated_at

    updated_at = property(get_updated_at, set_updated_at, None, "")


    
class EpisodeTextModel(object):
    def __init__(self, episode_id, text):
        self._episode_id = episode_id
        self._text = text

        self._changed = False
        
    @staticmethod
    def from_dict(source):
        episode_id = source["episode_id"]
        text = source["text"]

        return EpisodeTextModel(episode_id, text)

    def to_dict(self):
        return {
            "episode_id": self._episode_id,
            "text": self._text,
        }

    def is_changed(self):
        return self._changed

    # data get/put
    @staticmethod
    def get_collection():
        db = firestore.Client()
        return db.collection(EPISODE_TEXT_COLLECTION)

    @staticmethod
    def get(episode_id):
        ref = EpisodeTextModel.get_collection().document(episode_id).get()
        if not ref.exists:
            return None

        data = ref.to_dict()
        if "text" in data:
            data["text"] = zlib.decompress(data["text"]) # decompress
            data["text"] = data["text"].decode("utf-8") # from utf-8 bytes to unicode
        
        return EpisodeTextModel.from_dict(data)

    def put(self):
        data = self.to_dict()
        data["text"] = data["text"].encode("utf-8") # from unicode to utf-8 bytes
        data["text"] = zlib.compress(data["text"]) # compress
        EpisodeTextModel.get_collection().document(self._episode_id).set(data)

    # properties

    def get_episode_id(self):
        return self._episode_id

    def set_episode_id(self, episode_id):
        self._changed = self._changed or (self._episode_id != episode_id)
        self._episode_id = episode_id

    episode_id = property(get_episode_id, set_episode_id, None, "")

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._changed = self._changed or (self._text != text)
        self._text = text

    text = property(get_text, set_text, None, "")
