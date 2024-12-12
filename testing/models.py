from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=128)


class Crossref(models.Model):
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=256)
    doi = models.CharField(max_length=32)
    updated = models.DateTimeField()
