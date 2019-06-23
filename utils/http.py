
import json
import os
import re

import requests
from flask import request, url_for, redirect

from users.models import SessionModel

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

def require_session(redirect_login=True):
    def _decorator(func):
        def _body(*args, **kwargs):
            sm = None
            sid = request.cookies.get("session_id", None)

            if sid is not None and not re.match(r"^session_[A-Za-z0-9+-]+$", sid):
                sid = None

            fn = None
            if sid is not None:
                fn = "/tmp/%s.json" % sid

                if os.path.exists(fn):
                    fp = open(fn)
                    js = json.load(fp)
                    fp.close()

                    sm = SessionModel.from_dict(js)
                else:
                    sm = SessionModel.get(sid)

            if (sm is None) and redirect_login:
                print(url_for("kushimori.get_login"))
                return redirect(url_for("kushimori.get_login"))

            if (sm is not None) and (fn is not None) and (not os.path.exists(fn)):
                fp = open(fn, "w")
                # TODO: need to save DatetimeWithNanoseconds in json
                data = sm.to_dict()
                if "created_at" in data:
                    data["created_at"] = None
                fp.write(json.dumps(data))
                fp.close()

            kwargs["session"] = sm
            return func(*args, **kwargs)

        _body.__name__ = func.__name__
        return _body

    return _decorator
