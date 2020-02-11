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
    def lyrics_Username_not_null(self):
        if self.UserName == " ":
            return False
        else:
            return True

    def lyrics_SongName_not_null(self):

        if self.SongName == " ":
            return False
        else:
            return True

    def lyrics_lyric_not_null(self):
        if self.Lyric == " ":
            return False
        else:
            return True        
                
    def lyrics_Username__null(self):
        if self.UserName == " ":
            return True
        else:
            return False

    def lyrics_SongName__null(self):

        if self.SongName == " ":
            return True
        else:
            return False