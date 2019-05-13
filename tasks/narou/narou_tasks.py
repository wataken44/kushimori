
import re
from urllib.parse import urlparse

from flask import Blueprint, request
from bs4 import BeautifulSoup

from utils.http import Req, parse_request_parameter
from novels.models import NovelModel
from sites.narou.parser import NarouNovelIndexParser
from sites.narou.utils import get_novel_id_by_url

application = Blueprint('tasks/narou', __name__)

@application.route("/tasks/narou/get_novel_index", methods=['POST'])
def get_novel_index():
    url = parse_request_parameter(request, 'url')

    resp = Req.get(url)

    if resp.status_code != 200:
        # todo logging
        return '', 503

    parser = NarouNovelIndexParser(url, html=resp.text)

    novel = parser.parse_novel_info()
    novel["novel_id"] = get_novel_id_by_url(url)
    novel["url"] = url
    
    model = NovelModel.from_dict(novel)
    model.put()
    
    return str(parser.parse_episodes_info())
