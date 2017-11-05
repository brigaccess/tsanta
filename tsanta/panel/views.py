from django.shortcuts import render, redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from . import misc


@login_required
def index_view(request):

    context = {
        'app_version': settings.APP_VERSION
    }

    return render(request, 'panel/index.html', context)


def logout_view(request):

    logout(request)

    return redirect(settings.LOGIN_URL)


def login_view(request):

    context = {
        'loginpage': settings.LOGIN_URL,
        'error_message': None,
        'app_version': settings.APP_VERSION
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next', '/panel/')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(next_url)
            else:
                context['error_message'] = 'Пользователь не активен'
        else:
            context['error_message'] = 'Неправильный логин или пароль'

    return render(request, 'panel/login.html', context)


def signup_view(request):

    context = {
        'app_version': settings.APP_VERSION
    }

    return render(request, 'panel/signup.html', context)
