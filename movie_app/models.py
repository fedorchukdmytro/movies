from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=500)
    # year = models.CharField(max_length=500)
    rated = models.CharField(max_length=500)
    released = models.CharField(max_length=500)
    runtime = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    director = models.ManyToManyField(
        Director,
        related_name='movies'
    )
    writer = models.CharField(max_length=500)
    actors = models.ManyToManyField(
        Actor,
        related_name='movies'
    )
    plot = models.CharField(max_length=500)
    language = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    awards = models.CharField(max_length=500)


