from django.shortcuts import render
from .models import Project


def project_lists_view(request):
    projects = Project.objects.all().order_by('-year')
    return render(request, "content/project_lists.html")