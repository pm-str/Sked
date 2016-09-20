from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'description', ('start_time', 'length'), 'warning_time')

admin.site.register(Task, TaskAdmin)
