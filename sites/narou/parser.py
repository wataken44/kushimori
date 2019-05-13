
from bs4 import BeautifulSoup

class NarouNovelIndexParser(object):
    def parse(self, html=None, soup=None):
        if soup == None:
            soup = BeautifulSoup(html)

    def _parse_novel_info(self, soup):
        title = None

        title_elem = soup.find("p", class_="novel_title")
        if title_elem:
            title = title_elem.string
            
        author = None
        author_url = None
        author_elem = soup.find("div", class_="novel_writername")
        if author_elem:
            if len(author_elem.contents) == 1:
                # author does not have url
                author = author_elem.contents[0].strip().replace("作者：", "")
            else:
                author = author_elem.a.string
                author_url = author_elem.a.get('href')

        summary = None
        summary_elem = soup.find("div", id="novel_ex")
        if summary_elem > 0:
            summary = get_inner(summary_elem)
        
        return title, author, author_url, summary

    def _parse_episodes_info(self, soup):
        episodes = []

        info_elem = soup.find("div", class_="index_box")

        if info_elem is None:
            return episodes

        chapter_index = 0
        chapter_title = None
        
        for child in info_elem.children:
            if child.name == "div" and child.attrs.get("class") == "chapter_title":
                chapter_index += 1
                chapter_title = child.string

            if child.name == "dl" and child.attrs.get("class") == "novel_sublist2":
                # if no chapter_title, index should be 1
                if chapter_index == 0:
                    chapter_index = 1

                episode = {
                    "chapter_index": chapter_index,
                    "chapter_title": chapter_title,
                    "title": None,
                    "href": None,
                    "created_at": None,
                    "updated_at": None,
                }

            
        

class NarouNovelEpisodeParser(object):
    def parse(self, html):
        pass

