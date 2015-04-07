from django.db import models

class Board(models.Model):
    rid = models.CharField(max_length=16)
    title = models.CharField(max_length=128)
    about_text = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    
    # Author = Author

class Message(models.Model):
    title = models.TextField()
    text = models.TextField()
