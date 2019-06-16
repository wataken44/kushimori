
import re

from flask import Blueprint, request, jsonify

from google.auth.transport import requests as transport_requests
import google.oauth2.id_token

from users.models import UserModel, SessionModel
from utils.config import get_config
from utils.datetime import utcnow
from utils.http import parse_request_parameter
from utils.string import get_random_str

application = Blueprint('users', __name__)

@application.route("/session", methods=['POST'])
def create_session():
    token = parse_request_parameter(request, 'token')

    # check valid token
    req = transport_requests.Request()
    claims = google.oauth2.id_token.verify_firebase_token(token, req)
    if not claims:
        return 'Unauthorized', 401

    # check authorized users
    email = claims["email"]
    authorized_users = get_config("authorized_users")
    ok = False
    for au in authorized_users:
        ok = ok or (au["email"] == email)

    if not ok:
        return 'Unauthorized', 401

    # create user if not exist
    user_id = email
    um = UserModel.get(user_id)
    if um is None:
        name = email
        if "name" in claims:
            name = claims["name"]

        screen_name = re.sub(r"@.*", "", email)
        
        um = UserModel.from_dict({
            "user_id": user_id,
            "name": name,
            "email": email,
            "screen_name": screen_name,
        })
        um.put()

    # create session
    session_id = get_random_str("session_")
    sm = SessionModel.from_dict({
        "session_id": session_id,
        "user_id": user_id,
        "screen_name": um.screen_name,
        "created_at": utcnow()
    })
    sm.put()
    # todo: session cache
    
    return jsonify({"session": session_id})
