#!/usr/bin/python

import sys
import signal
from url_cleaner import removeBlackListedParameters


def sig_handle(signal, frame):
    sys.exit(0)

while True:
    signal.signal(signal.SIGINT, sig_handle)
    signal.signal(signal.SIGTERM, sig_handle)

    try:
        line = sys.stdin.readline().strip()
        urlList = line.split()
        urlInput = urlList[0]
        newUrl = removeBlackListedParameters(urlInput)
        sys.stdout.write('%s%s'.format(newUrl, '\n'))
        sys.stdout.flush()
    except Exception:
        continue
