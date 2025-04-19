from django.urls import path
from . import views

urlpatterns = [

    path('', views.project_lists_view, name='project_lists'),
]