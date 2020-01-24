from django.db import models
from django.contrib.auth.models import User

#class LyricManager(models.Manager):
    #pass


# Create your models here.
class Lyrics(models.Model):
    UserName = models.CharField(max_length=10)
    SongName = models.CharField(max_length=10)
    Lyric = models.TextField()
    #objects = LyricManager()
    def __str__(self):
        return self.UserName + ' ' + self.SongName + ' ' + self.Lyric 



             