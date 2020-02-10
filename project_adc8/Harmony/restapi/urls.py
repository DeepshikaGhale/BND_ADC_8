from django.urls import path
from .views import *

urlpatterns = [
    path('lyrics/',view_get_post_lyrics),
    path('lyrics/<int:ID>',view_getByID_updateByID_deleteByID),
]