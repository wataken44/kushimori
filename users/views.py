
from flask import Blueprint, request, jsonify

from google.auth.transport import requests as transport_requests
import google.oauth2.id_token

from utils.http import parse_request_parameter
from utils.string import get_random_str

application = Blueprint('users', __name__)

@application.route("/session", methods=['POST'])
def create_session():
    token = parse_request_parameter(request, 'token')

    req = transport_requests.Request()
    claims = google.oauth2.id_token.verify_firebase_token(token, req)
    if not claims:
        return 'Unauthorized', 401

    # TODO: check authorized user
    # TODO: if not exist create user
    # TODO: save session
    
    print(claims)
    
    return jsonify({"session": get_random_str("s/")})
