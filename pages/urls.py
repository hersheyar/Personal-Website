from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('newhome/', views.newhome, name='newhome'),

    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),

    path('experience/<slug:slug>/', views.experience_detail, name='experience_detail'),

    path('education/', views.education, name='education'),
]
