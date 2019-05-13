
from urllib.parse import urlparse
import re

SITE_INDEX="n01"

def get_novel_id(ncode):
    if ncode is None:
        return None
    return "%s-%s" % (SITE_INDEX, ncode)

def get_novel_id_by_url(url):
    n, e = _parse_url(url)
    return get_novel_id(n)

def get_episode_id(ncode, episode):
    e = episode
    if type(episode) == int:
        e = "%04d" % episode
    elif type(episode) == str and episode.isdigit() and episode.isascii():
        e = "%04d" % int(episode)
    return "%s-%s-%s" % (SITE_INDEX, ncode, e)

def get_episode_id_by_url(url):
    n, e = _parse_url(url)
    return get_episode_id(n, e)
    
def _parse_url(url):
    path = urlparse(url).path
    arr = path.split("/")

    ncode = None
    ep = None
    if len(arr) >= 2:
        ncode = arr[1]
    if len(arr) >= 3:
        ep = arr[2]

    return ncode, ep
        
