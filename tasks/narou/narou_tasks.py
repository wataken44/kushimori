
from flask import Blueprint, request
from bs4 import BeautifulSoup

from utils.http import Req, parse_request_parameter, get_inner

application = Blueprint('tasks/narou', __name__)

@application.route("/tasks/narou/get_novel_index", methods=['POST'])
def get_novel_index():
    url = parse_request_parameter(request, 'url')

    resp = Req.get(url)

    if resp.status_code != 200:
        # todo logging
        return '', 503
    
    soup = BeautifulSoup(resp.text)

    return u"%s\n%s\n%s\n%s" % parse_novel_info(soup)
    
def parse_novel_info(soup):
    title = None

    title_elems = soup.find_all("p", class_="novel_title")
    if len(title_elems) > 0:
        title = title_elems[0].string

    author = None
    author_url = None
    author_elems = soup.find_all("div", class_="novel_writername")
    if len(author_elems) > 0:
        ae = author_elems[0]
        if len(ae.contents) == 1:
            # author does not have url
            author = ae.contents[0].strip().replace("作者：", "")
        else:
            author = ae.a.string
            author_url = ae.a.get('href')

    summary = None
    summary_elems = soup.find_all("div", id="novel_ex")
    if len(summary_elems) > 0:
        summary = get_inner(summary_elems[0])
            
    return title, author, author_url, summary
    
    
    

    

    
