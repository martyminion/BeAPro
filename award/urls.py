from django.urls import path
from . import views

urlpatterns = [
  path('',views.welcome,name='welcome'),
  path('user/profile/',views.profile,name='profile'),
  path('new/profile/',views.new_profile,name='newprofile'),
  path('update/profile/',views.update_profile,name='updateprofile'),
  path('upload/project',views.upload_project, name='uploadproject'),
  path('single/project/<int:projectid>',views.singleproject,name='singleproject')
  
]