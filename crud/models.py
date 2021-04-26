from django.db import models


# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=20)
    released = models.CharField(max_length=30)
    runtime = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    writer = models.CharField(max_length=300)
    actors = models.CharField(max_length=300)
    plot = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    awards = models.CharField(max_length=300)
    poster = models.CharField(max_length=300)
    metascore = models.CharField(max_length=300)
    imdb_rating = models.CharField(max_length=300)
    imdb_votes = models.CharField(max_length=300)
    imdb_id = models.CharField(max_length=30)
    type = models.CharField(max_length=300)
    dvd = models.CharField(max_length=300)
    box_office = models.CharField(max_length=300)
    production = models.CharField(max_length=300)
    website = models.CharField(max_length=300)
    response = models.BooleanField()

    def __str__(self):
        return self


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self
