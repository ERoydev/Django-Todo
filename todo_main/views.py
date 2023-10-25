from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task


def home(request):
  
  tasks_objects = Task.objects.filter(is_completed=False).order_by('updated_at')

  context = {
    'tasks': tasks_objects
  }

  return render(request, 'home.html', context)