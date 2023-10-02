from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    tasks = Task.objects.all()  

    context = {
        'tasks': tasks
    }
    return render(request, 'todolist/home.html', context)

def classwork(request):
    tasks = Task.objects.all()  

    context = {
        'tasks': tasks
    }
    return render(request, 'todolist/classwork.html', context)

def grade(request):
    return render(request, 'todolist/grade.html')
def people(request):
   
    students = Student.objects.all()

    context = {
        'students': students 
    }
    return render(request, 'todolist/people.html', context)



