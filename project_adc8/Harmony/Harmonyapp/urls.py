

from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [ 
    path('Lyrics/',view_Lyrics_page), 
    path('Lyricsdata/',view_Lyrics_lists), 
    path('Lyricsform/',view_Lyrics_form),
    path('Lyricsform/save',view_Lyricsdata_save),
    path('Lyricsdata/edit/<int:ID>',view_Lyricsdata_updateform),
    path('Lyricsdata/edit/update/<int:ID>',view_update_form_data_in_db),
    #SignUp, Login, Logout
    path('signup/',view_register_user),
    path('login',view_login_user,name="login"),
    path('signup/logout/',view_logout,name="logout"),
    path('logout/',view_logout),
    path('signup/login.html',view_login_user,name="login"),
    path('Lyricsdata/delete/<int:ID>',view_lyrics_delete), 
    path('search/', search),
    path('index/',view_index,name="index")
]

