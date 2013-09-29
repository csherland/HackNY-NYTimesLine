from django.db import models

class Article(model.Model):
    date = models.DateTimeField()
    title = models.SlugField(max_length=255)
    picURL = models.URLField(max_length=511)
    description = models.TextField()

class Timeline(model.Model):
    query = models.CharField(max_length=255)
    articles = []
