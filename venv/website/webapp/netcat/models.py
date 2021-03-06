from django.db import models

# Create your models here.

class Movies(models.Model):
    TYPE = (
        ('movie', 'Movie'),
        ('series', 'Series')
    )

    GENRE = (
        ('Avontuur', 'Avontuur'),
        ('Bio', 'Bio'),
        ('Cabaret', 'Cabaret'),
        ('Cabaret ', 'Cabaret '),
        ('Caberet', 'Caberet'),
        ('Crime', 'Crime'),
        ('Docu', 'Docu'),
        ('Drama', 'Drama'),
        ('Familie', 'Familie'),
        ('Familiefilm', 'Familiefilm'),
        ('Familieserie', 'Familieserie'),
        ('Fantasie', 'Fantasie'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Kidneren', 'Kidneren'),
        ('Kinderen', 'Kinderen'),
        ('Kinderfilm', 'Kinderfilm'),
        ('Kinderserie', 'Kinderserie'),
        ('Komedie', 'Komedie'),
        ('Misdaad', 'Misdaad'),
        ('Musical', 'Musical'),
        ('Muziek', 'Muziek'),
        ('Oorlog', 'Oorlog'),
        ('Reality', 'Reality'),
        ('reality', 'reality'),
        ('Romance', 'Romance'),
        ('Romcom', 'Romcom'),
        ('Sci-fi', 'Sci-fi'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Sport', 'Sport'),
        ('Standup', 'Standup'),
        ('Stand-up', 'Stand-up'),
        ('Talkshow', 'Talkshow'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
        ('-', '-'),
        ("", ""),
    )
    name = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True, choices=GENRE)
    year = models.CharField(max_length=200, null=True)
    imdb = models.CharField(max_length=200, null=True)
    date_added = models.DateField(null=True)
    type = models.CharField(max_length=200, null=True, choices=TYPE)

    def __str__(self):
        return self.name

class Titles(models.Model):
    title = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    released = models.DateField(null=True)
    runtime = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    actors = models.CharField(max_length=200, null=True)
    director = models.CharField(max_length=200, null=True)
    writers = models.CharField(max_length=200, null=True)
    plot = models.CharField(max_length=500, null=True)
    language = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=500, null=True)
    awards = models.CharField(max_length=500, null=True)
    imdb = models.CharField(max_length=200, null=True)
    metascore = models.CharField(max_length=200, null=True)
    rotten_tomatoes = models.CharField(max_length=200, null=True)
    boxoffice = models.CharField(max_length=200, null=True)
    imdbid = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name