from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


def project_lists_view(request):
    projects = Project.objects.all().order_by('-year')
    return render(request, "content/project_lists.html")


def project_new_view(request):
    form = ProjectForm

    return render(request, "content/project_new.html", {"form":form})