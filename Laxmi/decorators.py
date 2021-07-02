from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.contrib.auth import authenticate, logout, login



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func




def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('working',allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('punch_page')
        return wrapper_func
    return decorator