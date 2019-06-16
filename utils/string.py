
import random

LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"

def get_random_str(prefix=None):
    s = ''.join(random.choices(LETTERS, k=32))
    if prefix:
        s = prefix + s
    return s
    
