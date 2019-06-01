
import re

def get_inner_text(tag):
    return ''.join(map(lambda c: str(c), tag.contents))

def remove_tag_p_br(text):
    text = text.replace("\r","")
    text = re.sub(r"<p[^>]*>", "", text)
    text = re.sub(r"</p>$", "", text, flags=re.MULTILINE)
    text = re.sub(r"</p>", "\n", text)
    text = re.sub(r"<br[^>]*>", "", text)
    return text
