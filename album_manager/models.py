from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False) 
    
    def __str__(self) -> str:
        return self.artist_name

class Album(models.Model):
    title = models.CharField(max_length=30, null=False)
    release_year = models.DateField()
    ALBUM_GENRE = {
        ('Metal', 'Metal'),
        ('Gótico', 'Gótico'),
        ('Rock', 'Rock'),
        ('Indie', 'Indie')
    }
    genre = models.CharField(max_length=30, choices=ALBUM_GENRE, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 
    picture = models.ImageField(upload_to='album_image')

    def __str__(self) -> str:
        return self.title

