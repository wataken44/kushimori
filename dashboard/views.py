
from flask import Blueprint, render_template, request

from users.models import SessionModel
from utils.http import require_session

application = Blueprint('dashboard', __name__)

@application.route("/dashboard/", methods=['GET'])
@require_session()
def get_list(session):    
    return render_template('index.html', session=session)

@application.route("/dashboard/edit", methods=['GET'])
def get_edit():
    return render_template('login.html')

@application.route("/dashboard/edit", methods=['POST'])
def post_edit():
    return render_template('login.html')

@application.route("/dashboard/follow_urls", methods=['GET'])
@require_session()
def get_follow(session):
    return render_template('follow_urls.html', session=session)

@application.route("/dashboard/follow_urls", methods=['POST'])
def post_follow():
    return render_template('login.html')
