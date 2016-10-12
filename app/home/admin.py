from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = (
        'user', 'name', 'description', ('start', 'end'), 'date',
        'repeat', ('time_notice', 'date_notice'), 'color', 'last_request'
    )

    def task_name(self, obj):
        return obj.name

    task_name.admin_order_field = 'name'
    list_display = ('name', 'full_datetime', 'is_request_today')
    list_filter = ('start', 'date', 'repeat', 'last_request')

admin.site.register(Task, TaskAdmin)
