#!/usr/bin/python3

import urllib.request as req
import sys

url = sys.argv[1]
if __name__ == "__main__":
    with req.urlopen(url) as resp:
        text = dict(resp.headers)
        text_id = text['X-Request-Id']

    print(text_id)
