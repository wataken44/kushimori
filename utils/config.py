
_debug = None

def set_debug(flag):
    global _debug
    if _debug is None:
        _debug = flag

def is_debug():
    return _debug

print(__file__)
