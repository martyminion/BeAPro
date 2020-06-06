from django.shortcuts import render,redirect
from .forms import ProfileForm,ProjectForm
from .models import Project,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
  title = "Be A Pro"
  return render(request,'welcome.html',{"title":title})

@login_required
def profile(request):
  current_user = request.user
  title = current_user + " Profile"
  user_profile = Profile.get_user_profile(current_user)
  context = {"title":title,"current_user":current_user,"user_profile":user_profile}
  return render(request,'profile/single_profile.html',context)

@login_required
def new_profile(request):
  title = "New Profile"
  current_user = request.user

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.cleaned_data['picture']
      bio = form.cleaned_data['bio']
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']

      user_profile = Profile.get_user_profile(current_user)
      user_profile.picture = image
      user_profile.bio = bio
      user_profile.first_name = first_name
      user_profile.last_name = last_name

      user_profile.save()

      return redirect(profile)
  else:
    form = ProfileForm()
  context = {"current_user":current_user,"title":title,"form":form}
  return render(request,'new_profile.html',context)

@login_required
def update_profile(request):
  title = "Update Profile"
  current_user = request.user

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.cleaned_data['picture']
      bio = form.cleaned_data['bio']
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']

      user_profile = Profile.get_user_profile(current_user)
      user_profile.picture = image
      user_profile.bio = bio
      user_profile.first_name = first_name
      user_profile.last_name = last_name

      user_profile.save()

      return redirect(profile)
  else:
    form = ProfileForm()
  context = {"current_user":current_user,"title":title,"form":form}
  return render(request,'update_profile.html',context)

