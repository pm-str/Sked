# coding: utf-8
from django.contrib import auth
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:current')
        else:
            args['login_error'] = u'Пользователь не найден'
            return render_to_response('loginsys/login.html', args)

    else:
        return render_to_response('loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('auth:login')
