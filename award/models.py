from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from statistics import mean
# Create your models here.

User = get_user_model()
class Profile(models.Model):
  picture = models.ImageField(upload_to = 'award/',blank=True)
  bio = models.TextField(blank=True)
  first_name = models.CharField(max_length=10,blank=True)
  last_name = models.CharField(max_length=10,blank=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  #save a profile
  def save_profile(self):
    self.save()
  
  def update_profile_bio(self,new_bio):
    self.profile_bio = new_bio
    self.save()
  
  def update_profile_photo(self,new_photo):
    self.profile_photo = new_photo
    self.save()
  
  def delete_profile(self):
    self.delete()

  @classmethod
  def get_user_profile(cls,userid):
    user_profile = cls.objects.get(user = userid)
    return user_profile

  def search_user_profile(search_term):
    user_profiles = User.objects.filter(username__icontains = search_term)
    return user_profiles

  def __str__(self):
    return self.user.username

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Project(models.Model):
  title = models.CharField(max_length=50,unique=True)
  landing_page = models.ImageField(upload_to = 'award/')
  description = models.TextField()
  live_site = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
  pub_date = models.DateTimeField(auto_now_add=True)
  
  @classmethod
  def get_single_project(cls,projectid):
    project = cls.objects.get(id = projectid)
    return project

  @classmethod
  def get_all_projects_user(cls,profileid):
    projects = cls.objects.filter(profile = profileid)
    return projects

  @classmethod
  def get_all_projects(cls):
    projects = cls.objects.all()
    return projects

  def __str__(self):
    return self.title

class Rating(models.Model):
  design = models.DecimalField(decimal_places=2,max_digits=4)
  usability = models.DecimalField(decimal_places=2,max_digits=4)
  content = models.DecimalField(decimal_places=2,max_digits=4)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  average = models.DecimalField(decimal_places=2,max_digits=4)

  @classmethod
  def get_project_ratings(cls,projectid):
    ratings = cls.objects.filter(project = projectid)
    return ratings

  def average_individual_ratings(self):
    average = (self.design + self.usability + self.content)/3
    return average

  def jury_average(projectid):
    projectratings = Rating.get_project_ratings(projectid)
    averagearr = []
    for projectrating in projectratings:
      averagearr.append(projectrating.average)
    avg = mean(averagearr)
    return round(avg,2)