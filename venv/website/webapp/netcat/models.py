from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    imdb = models.CharField(max_length=200, null=True)
    date_added = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name