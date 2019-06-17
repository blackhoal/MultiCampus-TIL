from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_origin = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    open_date = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    score = models.FloatField()
    poster_url = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
