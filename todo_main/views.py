from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task


def home(request):
  
  tasks_objects = Task.objects.filter(is_completed=False).order_by('updated_at')

  completed_tasks = Task.objects.filter(is_completed=True)
  context = {
    'tasks': tasks_objects,
    'completed': completed_tasks
  }

  return render(request, 'home.html', context)