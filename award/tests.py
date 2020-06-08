from django.test import TestCase
from award.models import User,Profile,Project,Rating
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime as dt

# Create your tests here.

class ProfileTest(TestCase):
  def setUp(self):
    self.user_kim = User.objects.create_user(username = 'Kimani', password = 'adminkim12345')
    
  def test_update_bio(self):
    self.user_kim.profile.update_profile_bio("We are the champions")
    self.assertEqual(self.user_kim.profile.profile_bio,"We are the champions")

  def test_search_user_profile(self):
    results =Profile.search_user_profile("Kimani")
    self.assertTrue(len(results)>0)

  def test_get_user_profile(self):
    userprof = Profile.get_user_profile(self.user_kim)
    self.assertEqual(userprof.user.username,self.user_kim.username)

class ProjectTest(TestCase):
  def setUp(self):
    self.user_kim = User.objects.create_user(username = 'Kimani', password = 'adminkim12345')
    self.new_project = Project(title = "Amazing",description = "Do you believe in magic",live_site = "amazing,org",profile = self.user_kim.profile, pub_date=dt.date.today())
    self.new_project.landing_page = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')

    self.new_project.save()

  def test_get_single_project(self):
    project = Project.get_single_project(self.new_project.id)
    self.assertEqual(self.new_project.title,"Amazing")

  def test_get_all_user_projects(self):
    projects = Project.get_all_projects_user(self.user_kim.profile)
    self.assertTrue(len(projects)==1)

  def test_get_all_projects(self):
    projects = Project.get_all_projects()
    self.assertTrue(len(projects)==1)

  def test_search_project_title(self):
    searched_projects = Project.search_project_title("Amazing")
    self.assertTrue(len(searched_projects)==1)

class RatingTest(TestCase):
  def setUp(self):
    self.user_kim = User.objects.create_user(username = 'Kimani', password = 'adminkim12345')
    self.new_project = Project(title = "Amazing",description = "Do you believe in magic",live_site = "amazing,org",profile = self.user_kim.profile, pub_date=dt.date.today())
    self.new_project.landing_page = SimpleUploadedFile(name='travel5.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/InstaClone/Instapic/media/travel5.jpg','rb').read(),content_type='image/jpeg')
    self.new_project.save()
    self.new_rating = Rating(design = 7, usability = 6, content = 5, profile = self.user_kim.profile, project = self.new_project )

    self.new_rating.average = self.new_rating.average_individual_ratings()
    self.new_rating.save()

  def test_get_project_ratings(self):
    ratings = Rating.get_project_ratings(self.new_project)
    self.assertTrue(len(ratings)==1)
  def test_average_ratings(self):
    self.assertEqual(self.new_rating.average,6)