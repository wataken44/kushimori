

from flask import Blueprint

application = Blueprint('task', __name__)

@application.route("/task")
def index():
    return 'this is task directory'

@application.route("/task/sample")
def sample():
    return 'sample'
