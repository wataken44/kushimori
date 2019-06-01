
from google.cloud import firestore

NOVEL_COLLECTION = u'novels'

class NovelModel(object):
    def __init__(self, novel_id, title, url, author, author_url, summary, episode_count):
        self._novel_id = novel_id
        self._title = title
        self._url = url
        self._author = author
        self._author_url = author_url
        self._summary = summary
        self._episode_count = episode_count

        self._changed = False
        
    # data get/put
    @staticmethod
    def get_collection():
        db = firestore.Client()
        return db.collection(NOVEL_COLLECTION)

    @staticmethod
    def get(novel_id):
        ref = NovelModel.get_collection().document(novel_id).get()
        if not ref.exists:
            return None
        return NovelModel.from_dict(ref.to_dict())

    def put(self):
        data = self.to_dict()
        NovelModel.get_collection().document(self._novel_id).set(data)
        
    @staticmethod
    def from_dict(source):
        novel_id = source["novel_id"]
        title = source["title"]
        url = source["url"]
        author = source["author"]
        author_url = source["author_url"]
        summary = source["summary"]
        episode_count = source["episode_count"]

        return NovelModel(novel_id, title, url, author, author_url, summary, episode_count)

    def to_dict(self):
        return {
            "novel_id": self._novel_id,
            "title": self._title,
            "url": self._url,
            "author": self._author,
            "author_url": self._author_url,
            "summary": self._summary,
            "episode_count": self._episode_count,
        }

    def assign(self, source):
        self.novel_id = source["novel_id"]
        self.title = source["title"]
        self.url = source["url"]
        self.author = source["author"]
        self.author_url = source["author_url"]
        self.summary = source["summary"]
        self.episode_count = source["episode_count"]
    
    def is_changed(self):
        return self._changed

    # properties

    def get_novel_id(self):
        return self._novel_id

    def set_novel_id(self, novel_id):
        self._changed = self._changed or (self._novel_id != novel_id)
        self._novel_id = novel_id

    novel_id = property(get_novel_id, set_novel_id, None, "")

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

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._changed = self._changed or (self._author != author)
        self._author = author

    author = property(get_author, set_author, None, "")

    def get_author_url(self):
        return self._author_url

    def set_author_url(self, author_url):
        self._changed = self._changed or (self._author_url != author_url)
        self._author_url = author_url

    author_url = property(get_author_url, set_author_url, None, "")

    def get_summary(self):
        return self._summary

    def set_summary(self, summary):
        self._changed = self._changed or (self._summary != summary)
        self._summary = summary

    summary = property(get_summary, set_summary, None, "")

    def get_episode_count(self):
        return self._episode_count

    def set_episode_count(self, episode_count):
        self._changed = self._changed or (self._episode_count != episode_count)
        self._episode_count = episode_count

    episode_count = property(get_episode_count, set_episode_count, None, "")

