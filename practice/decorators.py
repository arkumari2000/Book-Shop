from django.http import HttpResponse
from django.shortcuts import redirect


def decorator(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *arg, **kwargs)

    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *arg, **kwargs)
            else:
                return HttpResponse('you are not authorised person')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *arg, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user')
        if group == 'admin':
            return view_func(request, *arg, **kwargs)

    return wrapper_func
