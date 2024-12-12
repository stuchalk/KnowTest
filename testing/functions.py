# import json
import json
import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def crossref(src):
    crtmp = "https://api.crossref.org/works?query.title=*src*&filter=from-pub-date:2024-01-01"
    resp = requests.get(crtmp.replace("*src*", src)).json()
    items = resp["message"]["items"]
    hits = []
    for item in items:
        authstr = ""
        for au in item["author"]:
            if authstr != "":
                authstr += ", "
            authstr += au["family"]
        hits.append("'" + item["title"][0] + "'<br><em>" + authstr + "</em><br/>DOI:" + item["DOI"])
    print(hits)
    exit()


crossref("ferrocene")
