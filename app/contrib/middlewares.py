# coding: utf-8
from django.conf import settings
from django.contrib.auth.decorators import login_required

public_paths = {'/auth/login', '/admin/'}


class AuthRequiredMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if (request.path in public_paths):
            return
        else:
            return
            #return login_required(view_func)(request, *view_args, **view_kwargs)
