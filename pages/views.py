
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def projects(request):
    return render(request, 'pages/projects.html')

def experience(request):
    return render(request, 'pages/experience.html')

def experience_detail(request, slug):
    return render(request, f'experience_details/{slug}.html')

def education(request):
    return render(request, 'pages/education.html')

def education_detail(request, slug):
    return render(request, f'education_details/{slug}.html')

def contact(request):
    return render(request, 'pages/contact.html')