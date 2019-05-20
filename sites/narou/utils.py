
from urllib.parse import urlparse
import re

SITE_INDEX="n01"

def make_novel_id(ncode):
    if ncode is None:
        return None
    return "%s-%s" % (SITE_INDEX, ncode)

def make_episode_id(ncode, episode):
    e = episode
    if type(episode) == int:
        e = "%04d" % episode
    elif type(episode) == str and episode.isdigit() and episode.isascii():
        e = "%04d" % int(episode)
    return "%s-%s-%s" % (SITE_INDEX, ncode, e)

def get_site_novel_id(url):
    return parse_url(url)[0]

def get_site_episode_id(url):
    return parse_url(url)[1]

def get_novel_id_from_url(url):
    n, e = parse_url(url)
    return make_novel_id(n)

def get_episode_id_from_url(url):
    n, e = parse_url(url)
    return make_episode_id(n, e)
    
def parse_url(url):
    path = urlparse(url).path
    arr = path.split("/")

    ncode = None
    ep = None
    if len(arr) >= 2:
        ncode = arr[1]
    if len(arr) >= 3:
        ep = arr[2]

    return ncode, ep
        
