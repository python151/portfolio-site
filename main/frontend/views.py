from django.shortcuts import render
from .models import Project

def getAllProjects():
    projects = Project.objects.all()
    return projects


# Create your views here.
def index(request):
    return render(request, "index.html", {
        "projects": getAllProjects()
    })

def about(request):
    return render(request, "about.html")

def resume(request):
    return render(request, "resume.html")

def contact(request):
    return render(request, "contact.html")

def projects(request):
    return render(request, "projects.html", {
        "projects": getAllProjects()
    })

def project(request, id):
    return render(request, "project.html")