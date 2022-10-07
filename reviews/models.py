from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    img = models.ImageField()


class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
