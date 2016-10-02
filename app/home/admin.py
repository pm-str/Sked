from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = (
        'user', 'name', 'description', ('start', 'end'), 'date',
        'repeat', ('time_notice', 'date_notice'), 'color', 'last_request'
    )

admin.site.register(Task, TaskAdmin)
