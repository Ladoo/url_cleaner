#!/usr/bin/python

import sys
from stripper import removeBlackListedParameters


while True:
    line = sys.stdin.readline().strip()
    urlList = line.split(' ')
    urlInput = urlList[0]
    newUrl = removeBlackListedParameters(urlInput)
    sys.stdout.write('%s%s' % (newUrl, '\n'))
    sys.stdout.flush()
