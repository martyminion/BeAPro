from django.shortcuts import render,redirect
from .forms import ProfileForm,ProjectForm,RatingsForm
from .models import Project,Profile,Rating
from django.contrib.auth.decorators import login_required
import datetime as dt
#rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from award.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

def welcome(request):
  title = "Be A Pro"
  projects = Project.get_all_projects()
  

  return render(request,'welcome.html',{"title":title,"projects":projects})

@login_required
def profile(request):
  current_user = request.user
  title = current_user.username + " Profile"
  user_profile = Profile.get_user_profile(current_user)
  projects = Project.get_all_projects_user(user_profile)
  context = {"title":title,"current_user":current_user,"userprofile":user_profile,"projects":projects}
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
  return render(request,'profile/new_profile.html',context)

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
  return render(request,'profile/update_profile.html',context)

@login_required
def upload_project(request):
  title = "Project Upload"
  current_user = request.user
  user_profile = Profile.get_user_profile(current_user)
  if request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      new_project = form.save(commit=False)
      new_project.profile = user_profile
      new_project.pub_date = dt.date.today()
      new_project.save()
      return redirect(profile)
  else:
    form = ProjectForm()
  context = {"current_user":current_user,"title":title,"form":form}
  return render(request,'project/upload_project.html',context)

@login_required
def singleproject(request,projectid):
  project = Project.get_single_project(projectid)
  title = project.title
  ratings = Rating.get_project_ratings(project)

  return render(request, 'project/single_project.html', {"title":title,"project":project,"ratings":ratings})

@login_required
def rate_project(request,projectid):
  project = Project.get_single_project(projectid)
  title = "Rate " + project.title
  if request.method == 'POST':
    form = RatingsForm(request.POST)
    if form.is_valid():
      new_rating = form.save(commit=False)
      new_rating.profile = project.profile
      new_rating.project = project
      new_rating.average = new_rating.average_individual_ratings()

      new_rating.save()
      return redirect(singleproject,projectid = project.id)
  else:
    form = RatingsForm()
  context = {'title':title,'project':project,'form':form}
  return render(request,'project/rate_project.html',context)

class ProjectList(APIView):
  permission_classes = (IsAuthenticatedOrReadOnly)
  def get(self,request, format = None):
    all_projects = Project.get_all_projects()
    serializers = ProjectSerializer(all_projects,many = True)
    return Response(serializers.data)

class ProfileList(APIView):
  permission_classes = (IsAuthenticatedOrReadOnly)
  def get(self,request,format = None):
    all_profiles = Profile.objects.all()
    serializers = ProfileSerializer(all_profiles,many = True)
    return Response(serializers.data)

def search_project(request):
  title = "project search"
  if 'searchproject' in request.GET and request.GET["searchproject"]:
    searchproject = request.GET.get("searchproject")
    results = Project.search_project_title(searchproject)
    if len(results)>0:
      return render(request,'project/search_results.html',{"title":title,"results":results,"projectsearch":searchproject})
    else:
      message = "Could not find project with that title"
      return render(request,'project/search_results.html',{"title":title,"message":message,"projectsearch":searchproject})
  else:
    message = "Please enter a valid project title"
    return render(request,'project/search_results.html',{"title":title,"message":message,"namesearch":searchname})