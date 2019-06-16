
from flask import Blueprint, render_template, request

from users.models import SessionModel

application = Blueprint('kushimori', __name__)

@application.route("/", methods=['GET'])
def get_index():
    sm = None
    session_id = request.cookies.get("session_id", None)

    if session_id:
        sm = SessionModel.get(session_id)
    
    return render_template('index.html', session=sm)

@application.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')
