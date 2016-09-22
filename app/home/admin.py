from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'description', ('start_time', 'end_time'), 'warning_time', 'color')

admin.site.register(Task, TaskAdmin)
