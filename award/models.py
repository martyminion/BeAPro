from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model
class Profile(models.Model):
  picture = models.ImageField(upload_to = 'award/',blank=True)
  bio = models.TextField(blank=True)
  first_name = models.CharField(max_length=10,blank=True)
  last_name = models.CharField(max_length=10,blank=True)
  email = models.CharField(max_length=35,blank=True)


class Project(models.Model):
  title = models.CharField(max_length=50,)
  landing_page = models.ImageField(upload_to = 'award/')
  description = models.TextField()
  live_site = models.CharField(max_length=100)
  project = models.ForeignKey(Profile,on_delete=models.CASCADE)
