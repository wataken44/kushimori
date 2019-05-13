

from flask import Blueprint
from google.cloud import firestore

application = Blueprint('task', __name__)

@application.route("/task")
def index():
    return 'this is task directory'

@application.route("/task/sample")
def sample():

    db = firestore.Client()

    novels = db.collection(u'novels').order_by(u'novel_id').limit(100).get()

    body = ""
    for novel in novels:
        body += "%s %s<br>" % ( novel.to_dict()["novel_id"], novel.to_dict()["title"] )
    
    return '<html><body>%s</body></html>' % body
