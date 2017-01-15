# coding: utf-8
from django.contrib.auth.decorators import login_required

public_paths = {'/auth/login', '/celery_tasks/api/', '/english_words/api/'}


class AuthRequiredMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if any([request.path.startswith(path) for path in public_paths]):
            return
        else:
            return login_required(view_func)(request, *view_args, **view_kwargs)
