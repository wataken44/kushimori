
from flask import Blueprint, render_template

application = Blueprint('kushimori', __name__)

@application.route("/", methods=['GET'])
def get_novel_index():
    return render_template('index.html')


