
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from sites.narou.utils import get_site_novel_id, make_novel_id, make_episode_id
from utils.http import get_inner_text
from utils.datetime import get_datetime_from_jst, DAY_ONE

class NarouNovelIndexParser(object):
    def __init__(self, url, html=None, soup=None):
        self._url = url
        self._ncode = get_site_novel_id(url)
        self._soup = soup
        if soup == None:
            self._soup = BeautifulSoup(html, features="html.parser")

    def get_soup(self):
        return self._soup
            
    def parse_novel_info(self):
        title = None

        title_elem = self._soup.find("p", class_="novel_title")
        if title_elem:
            title = title_elem.string
            
        author = None
        author_url = None
        author_elem = self._soup.find("div", class_="novel_writername")
        if author_elem:
            if len(author_elem.contents) == 1:
                # author does not have url
                author = author_elem.contents[0].strip().replace("作者：", "")
            else:
                author = author_elem.a.string
                author_url = author_elem.a.get('href')

        summary = None
        summary_elem = self._soup.find("div", id="novel_ex")
        if summary_elem:
            summary = get_inner_text(summary_elem)

        episode_count = 1
        episodes_elems = self._soup.findAll("dl", class_="novel_sublist2")
        if episodes_elems:
            episode_count = len(episodes_elems)
            
        return {
            "novel_id": make_novel_id(self._ncode),
            "url": self._url,
            "title": title,
            "author": author,
            "author_url": author_url,
            "summary": summary,
            "episode_count": episode_count,
        }

    def parse_episodes_info(self):
        episodes = self._parse_multi_episodes_info()
        if episodes:
            return episodes

        return self._parse_single_episodes_info()
    
    def _parse_multi_episodes_info(self):
        info_elem = self._soup.find("div", class_="index_box")

        if info_elem is None:
            return None

        chapter_index = 0
        chapter_title = None
        
        episodes = []
        for child in info_elem.children:
            if child.name is None:
                continue

            if child.name == "div" and child.attrs.get("class") == ["chapter_title"]:
                chapter_index += 1
                chapter_title = child.string
                continue

            if child.name == "dl" and child.attrs.get("class") == ["novel_sublist2"]:
                # if no chapter_title, index should be 1
                if chapter_index == 0:
                    chapter_index = 1

                link_elem = child.find("a")

                title = link_elem.string
                href = urljoin(self._url, link_elem.attrs.get("href"))

                created_elem = child.find("dt")
                created_at = self._to_datetime(created_elem.contents[0].strip())

                updated_at = created_at
                updated_elem = created_elem.find("span")
                if updated_elem:
                    updated_at = self._to_datetime(re.sub(" [^ ]+$", "", str(updated_elem.attrs.get("title"))))
                
                episode = {
                    "episode_id": make_episode_id(self._ncode, len(episodes)),
                    "chapter_index": chapter_index,
                    "chapter_title": chapter_title,
                    "title": title,
                    "url": href,
                    "created_at": created_at,
                    "updated_at": updated_at
                }

                episodes.append(episode)
                continue

        return { "episodes" : episodes }

    def _parse_single_episodes_info(self):

        title_elem = self._soup.find("p", class_="novel_title")
        if title_elem:
            title = title_elem.string

        episode = {
            "episode_id": make_episode_id(self._ncode, 0),
            "chapter_index": 1,
            "chapter_title": "",
            "title": title,
            "url": self._url,
            "created_at": DAY_ONE,
            "updated_at": DAY_ONE
        }
        
        return { "episodes" : [episode] }
    
    def _to_datetime(self, s):
        a = re.split(r"[/ :]", s)
        return get_datetime_from_jst(int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]))

    
        

class NarouNovelEpisodeParser(object):
    def parse(self, html):
        pass

