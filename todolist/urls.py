from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classwork/', views.classwork, name='classwork'),
    path('grade/', views.grade, name='grade'),
    path('people/', views.people, name='people'),
    
]