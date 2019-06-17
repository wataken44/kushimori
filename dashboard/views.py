
from flask import Blueprint, render_template, request

from users.models import SessionModel

application = Blueprint('dashboard', __name__)

@application.route("/dashboard/", methods=['GET'])
def get_list():
    sm = None
    session_id = request.cookies.get("session_id", None)

    if session_id:
        sm = SessionModel.get(session_id)
    
    return render_template('index.html', session=sm)

@application.route("/dashboard/edit", methods=['GET'])
def get_edit():
    return render_template('login.html')

@application.route("/dashboard/edit", methods=['POST'])
def post_edit():
    return render_template('login.html')

@application.route("/dashboard/follow", methods=['GET'])
def get_follow():
    return render_template('login.html')

@application.route("/dashboard/follow", methods=['POST'])
def post_follow():
    return render_template('login.html')
