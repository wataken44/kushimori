
import requests

USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'

class Req:
    @classmethod
    def get(self, url, **kwargs):
        if 'headers' in kwargs:
            kwargs['headers']['USER-AGENT'] = USER_AGENT
        else:
            kwargs['headers'] = { 'USER-AGENT': USER_AGENT }

        return requests.get(url, **kwargs)


def parse_request_parameter(request, *args):
    ret = []
    if request.is_json:
        for arg in args:
            if arg in request.json:
                ret.append(request.json[arg])
            else:
                ret.append(None)
    else:
        for arg in args:
            ret.append(request.form.get(arg))

    # parse failed. return None
    if len(args) != len(ret):
        ret = [None] * len(args)

    if len(ret) == 1:
        return ret[0]
    else:
        return ret

def get_inner(tag):
    return ''.join(map(lambda c: str(c), tag.contents))
