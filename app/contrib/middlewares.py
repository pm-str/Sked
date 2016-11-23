# coding: utf-8
from django.contrib.auth.decorators import login_required

public_paths = {'/auth/login', '/celery/api/check_current_message'}


class AuthRequiredMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in public_paths:
            return
        else:
            return login_required(view_func)(request, *view_args, **view_kwargs)
