from urlparse import urlparse, parse_qs, urlunparse
from urllib import urlencode, unquote


def removeBlackListedParameters(url):
    parsedUrl = urlparse(url)
    queryStrings = parse_qs(parsedUrl.query, keep_blank_values=True)
    filtered = dict(
        (k, v)
        for k, v in queryStrings.iteritems()
        if not k.startswith('utm_') | k.startswith('mkt_') | k.startswith('gclid')
    )

    return urlunparse([
        parsedUrl.scheme,
        parsedUrl.netloc,
        parsedUrl.path,
        parsedUrl.params,
        unquote(urlencode(filtered, doseq=True)),
        parsedUrl.fragment,
    ])
