from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('description', 'is_completed', 'updated_at')
  search_fields= ('description',)
