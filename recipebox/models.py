"""
Author
    Name
    Bio

Recipe
    Author
    Title
    Description
    Time Required
    Instructions

"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    favorites = models.ManyToManyField(
        'Recipe', related_name='favorites', blank=True)
# https://stackoverflow.com/questions/49098606/how-to-save-a-users-favorite-posts-in-django


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"
