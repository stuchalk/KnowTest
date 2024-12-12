from django_unicorn.components import UnicornView
from testing.models import Crossref
from pytz import timezone
from datetime import datetime
import requests


local = timezone("America/New_York")


class CrossrefsrcView(UnicornView):
    src: str = ''
    debug: str = ''
    hits: list[dict] = []
    refs = Crossref.objects.none()

    def mount(self):
        self.refs = Crossref.objects.all()

    def get_refs(self):
        crtmp = "https://api.crossref.org/works?query.title=*src*&filter=from-pub-date:2024-01-01"
        crurl = crtmp.replace("*src*", self.src)
        resp = requests.get(crurl).json()
        items = resp["message"]["items"]
        for item in items:
            hit = {}
            hit.update({"title": item["title"][0]})
            if 'author' in item.keys():
                authstr = ""
                for au in item["author"]:
                    if authstr != "":
                        authstr += ", "
                    if 'family' in au.keys():
                        authstr += au["family"]
                    elif 'given' in au.keys():
                        authstr += au["given"]
                    else:
                        authstr += 'unknown'
            else:
                authstr = "No authors"

            hit.update({"authors": authstr})
            hit.update({"doi": item["DOI"]})
            self.hits.append(hit)

    def add_ref(self, doi):
        crurl = "https://api.crossref.org/works/" + doi
        resp = requests.get(crurl).json()
        ref = resp["message"]
        authstr = ""
        for au in ref["author"]:
            if authstr != "":
                authstr += ", "
            authstr += au["family"]
        Crossref.objects.create(title=ref['title'][0], authors=authstr, doi=ref["DOI"], updated=local.localize(datetime.now()))
        self.refs = Crossref.objects.all()
        self.src = ''

    def drop_ref(self, refid):
        Crossref.objects.filter(id=refid).delete()
        self.refs = Crossref.objects.all()
