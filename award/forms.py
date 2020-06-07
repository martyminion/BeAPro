from django import forms
from .models import Profile,Project,Rating

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['profile']

class RatingsForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['profile','project','average']