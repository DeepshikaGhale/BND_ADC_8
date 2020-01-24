from django.db import models

# Create your models here.

class Lyrics(models.Model):
    UserName = models.CharField(max_length=10)
    SongName = models.CharField(max_length=10)
    Lyric = models.TextField()

    def __str__(self):
        return self.UserName + ' ' + self.SongName + ' ' + self.Lyric 

