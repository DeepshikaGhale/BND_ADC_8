from django.db import models

class Users(models.Model):
       pic = models.ImageField(upload_to = 'profiles')