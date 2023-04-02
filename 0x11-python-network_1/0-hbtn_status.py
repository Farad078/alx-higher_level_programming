#!/usr/bin/python3
import urllib.request as req

url = "https://alx-intranet.hbtn.io/status"
with req.urlopen(url) as resp:
    html = resp.read()

print(f"Body response:")
print(f"    - type: {type(html)}")
print(f"    - utf8 content: {html.decode('utf-8')}")