
from flask import Blueprint, render_template, request

from users.models import SessionModel
from utils.http import require_session

application = Blueprint('kushimori', __name__)

@application.route("/", methods=['GET'])
@require_session(redirect_login=False)
def get_index(session):
    return render_template('index.html', session=session)

@application.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')
