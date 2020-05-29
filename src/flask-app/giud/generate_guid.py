import math
import calendar
import time

from .. import config as cfg

def get_short_guid() -> str:
    """ generate guid with epoch time stamp
    :return: string
    """
    time.sleep(1)
    idnum = calendar.timegm(time.gmtime())
    base = len(cfg.ALPHABET)
    out = []
    t = int(math.log(idnum, base))
    while True:
        bcp = int(pow(base, t))
        a = int(idnum / bcp) % base
        out.append(cfg.ALPHABET[a:a+1])
        idnum = idnum - (a * bcp)
        t -= 1
        if t < 0: break

    out = ''.join(out[::-1])
    
    return out