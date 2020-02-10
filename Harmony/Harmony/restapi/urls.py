from django.urls import path
from . import views

urlpatterns = [
    path('api/pagination/<int:PAGENO>/<int:SIZE>/', views.api_pagination, name='list_Lyric_pagination'),
    path('api/',views.view_get_post_lyrics),
    path('api/<int:ID>/',views.view_getByID_updateByID_deleteByID),
    #pagination
    
]