from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index , name = 'index'),
    path('upload', views.uploadImage , name = 'uploadImage'),
    path("download_image", views.download_image , name = "download_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
