#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request as req

url = "https://alx-intranet.hbtn.io/status"
with req.urlopen(url) as resp:
    html = resp.read()

print(f"Body response:")
print(f"\t- type: {type(html)}")
print(f"\t- content: {html}")
print(f"\t- utf8 content: {html.decode('utf-8')}")
