from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model
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
  title = models.CharField(max_length=50,)
  landing_page = models.ImageField(upload_to = 'award/')
  description = models.TextField()
  live_site = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

