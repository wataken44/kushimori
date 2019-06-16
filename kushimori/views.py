
from flask import Blueprint, render_template

application = Blueprint('kushimori', __name__)

@application.route("/", methods=['GET'])
def get_index():
    return render_template('index.html')

@application.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')
