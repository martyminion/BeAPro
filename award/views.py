from django.shortcuts import render

# Create your views here.

def welcome(request):
  title = "Be A Pro"
  return render(request,'welcome.html',{"title":title})