
import json
import os
import sys

_config = None

def load_config():
    global _config

    fn = os.path.abspath(os.path.dirname(__file__) + "/../config.json")

    fp = open(fn)
    _config = json.load(fp)
    fp.close()

def get_config(key = None):
    global _config
    if key:
        if key in _config:
            return _config[key]
        return None
    else:
        return _config
