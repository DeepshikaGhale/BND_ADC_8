from django.test import TestCase

# Create your tests here.
from . models import Lyrics
# Create your tests here.
class test_username(TestCase):
    def test_lyrics_Username_not_null(self):
        lyricss = Lyrics.objects.create(UserName="Ram", SongName="najik", Lyric="dsv 7ik6umnfbyjk,mjnby kjgnbvj,jkmjhnbmkjhngfbgmk j hnbvmjnhbgvkjhgnbcvh")
        self.assertTrue(lyricss.lyrics_Username_not_null())
    
    def test_lyrics_SongName_not_null(self):
        lyricss1 = Lyrics.objects.create(UserName="Shyam", SongName="Blue Sea", Lyric="svnbhldngodbh4noiegnorifubhegodikbroiktbhngeoilvxknblkhrnhegsl")
        self.assertTrue(lyricss1.lyrics_SongName_not_null())
    
   
    def test_lyrics_lyric_not_null(self):
        lyricss2 = Lyrics.objects.create(UserName="Sita", SongName="Pani Sea", Lyric="svnbhldngodbh4noiegnorifubhegodikbroiktbhngeoilvxknblkhrnhegsl")
        self.assertTrue(lyricss2.lyrics_lyric_not_null())    

    def test_lyrics_Username__null(self):
        lyricss3 = Lyrics.objects.create(UserName=" ", SongName="Blue Sea", Lyric="svnbhldngodbh4noiegnorifubhegodikbroiktbhngeoilvxknblkhrnhegsl")
        self.assertTrue(lyricss3.lyrics_SongName_not_null())


    def test_lyrics_SongName__null(self):
        lyricss4 = Lyrics.objects.create(UserName="Shyam", SongName=" ", Lyric="svnbhldngodbh4noiegnorifubhegodikbroiktbhngeoilvxknblkhrnhegsl")
        self.assertFalse(lyricss4.lyrics_SongName_not_null())     