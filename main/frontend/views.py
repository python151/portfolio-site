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
    project = Project.objects.filter(id=id)
    if not project.exists():
        return render(request, "404.html")
    return render(request, "project.html", {
        "project": project.get()
    })