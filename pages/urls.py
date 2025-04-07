from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),

    path('experience/<slug:slug>/', views.experience_detail, name='experience_detail'),

    path('education/', views.education, name='education'),

    path('education/<slug:slug>/', views.education_detail, name='education_detail'),

    path('contact/', views.contact, name='contact'),
]
