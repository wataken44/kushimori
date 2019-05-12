
from google.cloud import firestore

NOVEL_COLLECTION = u'novels'

class NovelModel(object):
    def __init__(self, novel_id, title, url, author, author_url, summary):
        self._novel_id = novel_id
        self._title = title
        self._url = url
        self._author = author
        self._author_url = author_url
        self._summary = summary

        self._changed = False


    # data create/read/update/delete

    def update(self):
        db = firestore.Client()
        data = self.to_dict()
        db.collection(NOVEL_COLLECTION).document(self._novel_id).set(data)
        
    # converters
        
    @staticmethod
    def from_dict(source):
        novel_id = source["novel_id"]
        title = source["title"]
        url = source["url"]
        author = source["author"]
        author_url = source["author_url"]
        summary = source["summary"]

        return NovelModel(novel_id, title, url, author, author_url, summary)

    def to_dict(self):
        return {
            "novel_id": self._novel_id,
            "title": self._title,
            "url": self._url,
            "author": self._author,
            "author_url": self._author_url,
            "summary": self._summary,
        }
    
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
