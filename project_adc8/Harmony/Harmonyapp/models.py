from django.db import models
from django.contrib.auth.models import User

#class LyricManager(models.Manager):
    #pass


# Create your models here.
class Music(models.Model):
    MusicType = models.CharField(max_length=100)
    SongName = models.CharField(max_length=100)
    Music_User = models.ManyToManyField(User)

    
    #objects = LyricManager()
    def __str__(self):
        return self.MusicType + ' ' + self.SongName 


class Artist(models.Model):
    Name = models.CharField(max_length=100)
    Age= models.IntegerField()
    Address = models.CharField(max_length=100)
    Songs = models.CharField(max_length=100)
    Artist_Music = models.ManyToManyField(Music)
    #objects = LyricManager()
    def __str__(self):
        return self.Name + ' ' + self.Age + ' ' + self.Address + ' ' + self.Songs




class Lyrics(models.Model):

    UserName = models.CharField(max_length=100)
    SongName = models.CharField(max_length=100)
    Lyric = models.TextField()
    Lyrics = models.ManyToManyField(User)
    music_lyrics = models.ForeignKey(Music, on_delete=models.CASCADE)
    #objects = LyricManager()
    def __str__(self):
        return self.UserName + ' ' + self.SongName + ' ' + self.Lyric 


class Users(models.Model):
    UserName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    User = models.ManyToManyField(Music)
    Users = models.ManyToManyField(Lyrics)
    #objects = LyricManager()
    def __str__(self):
        return self.UserName + ' ' + self.email + ' ' + self.address

