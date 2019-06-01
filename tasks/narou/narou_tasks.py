
import re
from urllib.parse import urlparse

from flask import Blueprint, request
from bs4 import BeautifulSoup

from utils.http import Req, parse_request_parameter
from novels.models import NovelModel
from episodes.models import EpisodeModel, EpisodeTextModel
from sites.narou.parser import NarouNovelIndexParser, NarouNovelEpisodeParser

application = Blueprint('tasks/narou', __name__)

@application.route("/tasks/narou/get_novel_index", methods=['POST'])
def get_novel_index():
    url = parse_request_parameter(request, 'url')

    resp = Req.get(url)

    if resp.status_code != 200:
        # todo: logging
        return '', 503

    parser = NarouNovelIndexParser(url, html=resp.text)

    novel = parser.parse_novel_info()

    # todo: create attr class
    nm = NovelModel.get(novel["novel_id"])
    if nm:
        nm.assign(novel)
        if nm.is_changed():
            nm.put()
    else:
        nm = NovelModel.from_dict(novel)
        nm.put()

    episodes = parser.parse_episodes_info()

    # todo: use batch write
    # todo: enqueue get_body when updated
    # todo: create attr class
    # todo: single episode
    # todo: maybe cause DeadlineExceededException
    for episode in episodes["episodes"]:
        em = EpisodeModel.get(episode["episode_id"])
        if em:
            em.assign(episode)
            if em.is_changed():
                em.put()
        else:
            em = EpisodeModel.from_dict(episode)
            em.put()
        
    return str(parser.parse_episodes_info())

@application.route("/tasks/narou/get_episode_text", methods=['POST'])
def get_episode_text():
    episode_id = parse_request_parameter(request, 'episode_id')
    url = parse_request_parameter(request, 'url')

    resp = Req.get(url)

    if resp.status_code != 200:
        # todo: logging
        return '', 503

    parser = NarouNovelEpisodeParser(url, html=resp.text)

    episode = parser.parse()
    episode["episode_id"] = episode_id

    em = EpisodeTextModel.get(episode_id)
    if em:
        em.assign(episode)
        if em.is_changed():
            em.put()
    else:
        em = EpisodeTextModel.from_dict(episode)
        em.put()
    
    return str(episode)
